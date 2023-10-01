import io
from typing import Dict

import xlsxwriter
from django.db.models import QuerySet
from django.http import HttpResponse

HEADERS = {0: 'Модель', 1: 'Версия', 2: 'Количество за неделю'}


def statistic_file(
    statistic: Dict[str, QuerySet],
) -> HttpResponse:
    """Загрузка файла статистики по роботам за неделю.

    Args:
        statistic: Словарь с моделями роботов и их количеством.

    Returns:
        HttpResponse с файлом со статистикой по роботам за неделю.
    """
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    workbook.formats[0].set_font_size(14)
    workbook.formats[0].set_font_name('Times New Roman')
    for model, robots in statistic.items():
        worksheet = workbook.add_worksheet(model)
        worksheet.set_column(0, 2, 20)
        for column, header in HEADERS.items():
            worksheet.write(0, column, header)
        row = 0
        for robot in robots:
            row += 1
            worksheet.write(row, 0, model)
            worksheet.write(row, 1, robot.get('version'))
            worksheet.write(row, 2, robot.get('amount'))
    workbook.close()
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type=(
            'application/vnd.openxmlformats'
            '-officedocument.spreadsheetml.sheet'
        ),
    )
    response['Content-Disposition'] = 'attachment; filename=statistic.xlsx'
    output.close()
    return response
