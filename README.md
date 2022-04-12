1. Установите зависимости. Советую использовать venv.
```
cd chesselo
pip install -r requirements.txt
```
2. Установите и запустите [Redis](https://redis.io/docs/getting-started/).
```
redis-start
```
3. Выполните миграцию и запустите сервер.
```
cd chesselo
python manage.py migrate 
python manage.py runserver
```
