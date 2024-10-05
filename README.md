# Link Storage API

## Описание

API для хранения и управления пользовательскими ссылками и коллекциями.

## Технологии

- Python 3.12+
- Django 5.0+ (Django Rest Framework)
- PostgreSQL
- Docker
- Swagger
- BeautifulSoup4
 

## Установка и запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Настройка окружения

Убедитесь, что у вас установлен Docker. Если нет, следуйте инструкциям по
установке [здесь](https://docs.docker.com/get-docker/).

### 3. Запуск Docker контейнеров

Запустите Docker контейнеры с помощью команды:

```bash
docker-compose up --build
```

### 4. Применение миграций

После того как контейнеры будут запущены, примените миграции:

```bash
docker-compose exec web python manage.py migrate
```

### 5. Создание суперпользователя

Создайте суперпользователя для доступа к админ панели:

```bash
docker-compose exec web python manage.py createsuperuser
```

### 6. Ссылки

- Админ панель: [http://localhost:8000/admin](http://localhost:8000/admin)
- Swagger документация: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

### 7. Запрос, который выводит 10 пользователей, у которых максимальное количество сохраненных ссылок, если количество ссылок одинаково у нескольких пользователей, выведете тех, кто раньше был зарегистрирован.

```SQL
SELECT u.id, u.email, COUNT(l.id) as links_count
FROM users_xone_user u
LEFT JOIN api_xone_link l ON u.id = l.user_id
GROUP BY u.id, u.email
ORDER BY COUNT(l.id) DESC, u.date_joined ASC
LIMIT 10;
```

## Автор

- Борщ Владислав - [FSOCllDRUG](https://github.com/FSOCllDRUG)

