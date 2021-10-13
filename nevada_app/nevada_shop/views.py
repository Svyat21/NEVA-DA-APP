from django.shortcuts import render
from django.views.generic import View
import logging

logger = logging.getLogger(__name__)


class HomeView(View):

    def get(self, request):
        context = {
            'title_html': 'Главная',
        }
        return render(request, 'nevada_shop/index.html', context=context)
