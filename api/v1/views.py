import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.v1.forms import RobotForm


@csrf_exempt
@require_http_methods(['POST'])
def create_robot(request: HttpRequest) -> HttpResponse:
    """Создание нового робота в базе данных.

    Args:
        request: Передаваемый запрос.

    Returns:
        Данные об ошибках: в случае неудачи создания.
        Данные о роботе: в случае успешного создания.
    """
    json_data = json.loads(request.body)
    form = RobotForm(json_data or None)
    if not form.is_valid():
        return JsonResponse(form.errors)
    form.instance.serial = json_data['model'] + '-' + json_data['version']
    form.save()
    return JsonResponse(json_data)
