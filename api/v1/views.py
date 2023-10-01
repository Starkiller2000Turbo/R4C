from datetime import datetime, timedelta

from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core.utils import statistic_file
from robots.models import Robot


@csrf_exempt
@require_http_methods(['GET'])
def download_statistic(request: HttpRequest) -> HttpResponse:
    """Загрузка файла статистики по роботам за неделю.

    Args:
        request: Передаваемый запрос.

    Returns:
        HttpResponse с файлом со статистикой по роботам за неделю.
    """
    models = (
        Robot.objects.filter(created__gte=datetime.now() - timedelta(days=7))
        .values_list('model', flat=True)
        .distinct()
        .order_by('model')
    )
    statistic = {
        model: Robot.objects.filter(model=model)
        .annotate(amount=Count('version'))
        .values('version', 'amount')
        for model in models
    }
    return statistic_file(statistic)
