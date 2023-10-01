import logging
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot

MESSAGE = """Добрый день!\n
Недавно вы интересовались нашим роботом модели {}, версии {}.\n
Этот робот теперь в наличии. Если вам подходит этот
 вариант - пожалуйста, свяжитесь с нами"""


@receiver(pre_save, sender=Robot)
def send_emails(sender: Robot):
    logging.debug("======================================")
    model = sender.model
    version = sender.version
    send_mail(
        '-'.join([model, version]),
        MESSAGE.format(model, version),
        'settings.EMAIL_HOST_USER',
        'maksim_ermoshin@mail.ru'
        fail_silently=False,
    )
