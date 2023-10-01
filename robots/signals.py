from typing import Any

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot

SUBJECT = """Покупка робота {}"""

MESSAGE = """Добрый день!\n
Недавно вы интересовались нашим роботом модели {}, версии {}.\n
Этот робот теперь в наличии. Если вам подходит этот вариант - \
     пожалуйста, свяжитесь с нами"""


@receiver(post_save, sender=Robot)
def send_emails(sender: Robot, instance: Robot, **kwargs: Any) -> None:
    """Отправление сообщений пользователям при создании робота.

    Args:
        sender: абстрактная модель робота.
        instance: модель созданного робота.
        **kwargs: прочие аргументы
    """
    send_mail(
        SUBJECT.format(instance.serial),
        MESSAGE.format(instance.model, instance.version),
        'settings.EMAIL_HOST_USER',
        list(
            Order.objects.filter(robot_serial=instance.serial).values_list(
                'customer__email',
                flat=True,
            ),
        ),
        fail_silently=False,
    )
