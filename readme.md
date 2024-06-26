# Product seller
## Описание проекта
Проект proiduct seller позволяет создавать, выбирать продукты и добавлять их в корзину. Реализованы Категории продуктов и их Под-категории.
### Содержанеие

- [Технологии](#tech)
- [Начало работы](#begining)
- [FAQ](#faq)
- [Комнада проекта](#team)

## <a name="tech">Технологии</a>

- [Django](https://www.djangoproject.com/)
- [Django REST](https://www.django-rest-framework.org/)

## <a name="begining">Начало работы</a>

### Начало работы

Активируйте вирутальное окржуние:

```
python -m venv venv
```

### Установка зависимостей

Установите зависимости из файла *requirements.txt*:

```
pip install -r requirements.txt
```

Если вы работаете локально, в файле .env установите:
*.env*
```
TEST_DATABASE = TRUE
```

### Установка зависимостей

Активируйте виртуальное окружение

```
source venv/sqripts/activate
```

Применение миграций и первый запуск:

```
python manage.py migrate
```

### Запуск сервера

Запустите проект:

```
python manage.py runserver
```

## <a name="faq">FAQ</a>

### Реализация изменения количества продуктов

Выплняется путем добавления продукта в корзину или его удаления из неё

### Программа вывода последовательности

Название - n_elements.py

## <a name="team">Команда проектка</a>

- Паршин Денис - backend developer