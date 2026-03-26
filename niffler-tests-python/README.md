## **Проект автотестов приложения  Niffler**

## 📋 О проекте

Проект представляет собой комплексный фреймворк для тестирования приложения Niffler. Он включает в себя:

- ✅ **UI тесты** с использованием Playwright
- ✅ **API тесты** (REST) с поддержкой OAuth 2.0
- ✅ **gRPC тесты** для проверки микросервисной коммуникации
- ✅ **Kafka тесты** для проверки событийной архитектуры
- ✅ **SOAP тесты** для проверки XML веб-сервисов
- ✅ Интеграция с **Allure Reports** для наглядной отчётности
- ✅ Работа с **базами данных** через SQLAlchemy
- ✅ Мокирование внешних сервисов через **WireMock**

## 🛠 Технологический стек

| Категория | Технологии                     |
|-----------|--------------------------------|
| **Язык** | Python 3.11+                   |
| **Тестирование** | Pytest, Allure                 |
| **UI Автоматизация** | Playwright                     |
| **API Клиенты** | Requests                       |
| **Работа с данными** | Pydantic, SQLAlchemy, SQLModel |
| **Базы данных** | PostgreSQL (через psycopg2)    |
| **Брокеры сообщений** | Confluent Kafka                |
| **Мокирование** | WireMock (для gRPC)            |
| **Генерация данных** | Mimesis                        |
| **Утилиты** | Python-dotenv, Jinja2, Curlify |

## 🚀 Настройка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/AlexLumen/niffler-py-st3.git
```
### 2. Запуск контейнеров

```bash
./docker-compose-dev.sh
```

### 3. Установка зависимостей
```bash
# Переход в директорию с тестами
cd niffler-py-st3/niffler-tests-python

# Установка Poetry
pip install poetry

# Установка зависимостей проекта
poetry install
```

### 3. Настройка переменных окружения
```env
USER_NAME="your_username"
PASSWORD="your_password"
FRONT_URL="http://frontend.niffler.dc"
AUTH_URL="http://auth.niffler.dc:9000"
GATEWAY_URL="http://gateway.niffler.dc:8090"
SPEND_DB_URL="postgresql://user:password@localhost:5432/niffler_spend"
AUTH_DB_URL="postgresql://user:password@localhost:5432/niffler_auth"
USERDATA_DB_URL="postgresql://user:password@localhost:5432/niffler_userdata"
KAFKA_BOOTSTRAP_SERVERS="localhost:9093"

```

### 4. Запуск тестов
```bash
# Запуск тестов с сохранением результатов Allure
poetry run pytest --alluredir=./allure-results

# Только UI тесты
poetry run pytest tests/ui_tests

# Только API тесты
poetry run pytest tests/api_tests

# Только gRPC тесты
poetry run pytest tests/grpc_tests

# Только Kafka тесты
poetry run pytest tests/kafka_tests

# Только SOAP тесты
poetry run pytest tests/soap_tests
```

### 5. Просмотр отчета
```bash
# Открыть отчёт в браузере
allure serve allure-results
```

## 🔄 CI/CD (GitHub Actions)
```text
Проект настроен на автоматическое выполнение тестов через GitHub Actions при каждом pull request в ветку main, 
 а так же доступен ручной запуск через интерфейс GitHub.
```
