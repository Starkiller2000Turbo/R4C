### Проект R4C - Robots for consumers

### Описание:

Это сервис, который ведёт учет произведенных роботов,а также выполняет операции,
связанные с этим процессом.

Разрабатывался исключительно на Django (без использования DRF).

Каждый робот(**Robot**) имеет определенную модель, выраженную двух-символьной 
последовательностью(например R2). Одновременно с этим, модель имеет различные 
версии(например D2). Так же у роботов есть серийный номер, объединяющий в себе
модель и версию(например R2-D2).

Покупатели(**Customer**) представлены своим email.

Заказы покупателей(**Order**) попадают в список ожидания, пока не появится требуемый робот.


### Как запустить проект:

Клонируйте репозиторий:
```
git clone git@github.com:Starkiller2000Turbo/R4C.git
```

Измените свою текущую рабочую дерикторию:
```
cd /R4C/
```

Создайте и активируйте виртуальное окружение

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Обновите pip:
```
python -m pip install --upgrade pip
```

Установите зависимости из requirements.txt:

```
pip install -r requirements.txt
```

Создайте миграции и запустите сервер:

```
make
```

### Как cкачать Excel-файл со сводкой по суммарным показателям производства роботов за последнюю неделю:
Сделайте GET запрос на эндпоинт "api/download_statistic/" 


### Эндпоинты:

| Эндпоинт              |Тип запроса| Тело запроса          | Ответ                           |
|-----------------------|-----------|-----------------------|---------------------------------|
|api/download_statistic/|GET        |--пусто--              | Файл данных о роботах за неделю |

### Авторы:

- :white_check_mark: [Starkiller2000Turbo](https://github.com/Starkiller2000Turbo)

### Стек технологий использованный в проекте:

- Python
- Django
- XlsxWriter
