### REST API для Bewise.ai

![image]({https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue})
![image]({https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white})
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image]({https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white})

Инструкция по развертыванию:
1. Для запуска потребуется Docker. [Get Docker](https://docs.docker.com/get-docker/)

2. Клонировать репозиторий и перейти в папку с проектом:
    ```
    git clone https://github.com/m00nrock/bewise_interview.git
    ```

    ```
    cd bewise_interview/
    ```

3. Запустите проект используя docker-compose
    ```
    cd infra/
    ```
    
    ```
    docker-compose up
    ```
    ###### проект запустится по адресу localhost:5000

### Технологии:
- Python 3.8.9
- Fask
- SQLAlchemy
- Docker + docker-compose
- PostgreSQL
- gunicorn

### Эндпойнты

localhost:5000/questions/ принимает POST запрос с содержимым
```
{
    "questions_num": integer
}
```

В ответ возвращает последнюю добавленную запись вида

```
{
    "added_at": "Thu, 05 May 2022 20:59:53 GMT",
    "date": "2014-02-11T23:18:29.298Z",
    "id": 53009,
    "text_answer": "Lake Maracaibo",
    "text_question": "In 1957 a deep channel was completed allowing ocean ships to reach this largest Venezuelan lake"
}
```

Пример запроса из терминала:

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"questions_num": 10}' \
  http://127.0.0.1:5000/questions/
```

Ответ в интерфейсе терминала:

```
{"added_at":"Thu, 05 May 2022 21:00:06 GMT","date":"2014-02-11T23:18:54.553Z","id":53565,"text_answer":"<i>The Six Million Dollar Man</i>","text_question":"\"A Bionic Christmas Carol\""}
```