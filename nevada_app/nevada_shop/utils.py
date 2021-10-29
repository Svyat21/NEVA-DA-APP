from django.core.mail import send_mail


def feedback_message(dict_message: dict):
    message = f"Заказан звонок от пользователя:\n{dict_message['name']}\n" \
              f"Номер телефона:\n{dict_message['phone']}\n"
    if dict_message.get('question'):
        message += f"Вопрос от пользователя:\n{dict_message['question']}"
    send_mail(
        subject=f"Заказ обратной связи от пользователя {dict_message['name']}",
        message=message,
        from_email='no-reply@nevada-band.ru',
        recipient_list=['sursvyat@gmail.com', 'neva-da-band@yandex.ru'],
        fail_silently=False,
    )
