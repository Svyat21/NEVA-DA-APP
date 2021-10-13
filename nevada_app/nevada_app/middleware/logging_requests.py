from django.http.request import HttpRequest
from django.utils.log import request_logger


class LoggUserRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            request.META['user_ip'] = x_forwarded_for.split(',')[0]
        else:
            request.META['user_ip'] = request.META.get('REMOTE_ADDR')

        context = {
            'user_ip': request.META.get('user_ip'),
            'path': request.path,
            'path_info': request.path_info,
            'request_method': request.method,
        }

        request_logger.info('Request processed', extra=context)

        response = self.get_response(request)
        return response
