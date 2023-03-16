
# Проект Yatube_API

Социальная сеть для блогеров. 
В проекте можно:
- Делать посты
- Оставлять комментарии
- Подписываться на авторов


## Установка проекта:

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/AntonVoronovYAR/api_final_yatube.git

cd yatube_api
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Выполнить миграции:
```bash
python manage.py migrate

python manage.py runserver
```
## Примеры запросов API

#### Пролучение публикаций

```http
  GET api/v1/posts/
```

#### Создание публикаций

```http
  POST /api/v1/posts/
```

#### Просмотр конкретной публикации

```http
  GET /api/v1/posts/1/
```



