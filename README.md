# test_task

Сборка:
```
docker-compose up --build
```


Список статей:
```
curl http://127.0.0.1:8000/api/articles/
```
Список комментариев:
```
curl http://127.0.0.1:8000/api/comments/ 

Создать статью:
```
curl -X POST http://127.0.0.1:8000/api/article/ -H 'Content-Type: application/json' -d '{"name":"nadasdasdme","text":"TEXT"}'
```

Создать комментарий к статье:
```
curl -X POST http://127.0.0.1:8000/api/comment/ -H 'Content-Type: application/json' -d '{"text": "топ","article": 1,"user": 1}'
```


http://127.0.0.1:8000/api/doc/ - документация по API



