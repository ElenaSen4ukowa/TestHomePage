ТЕСТОВОЕ ЗАДАНИЕ

WEB форма регистрации и авторизации
___
Требование к ПО: наличие установленого и запущенного docker

Установка:

Скачиваем vm_docker_ui.7z и распаковываем архив

В папке с распакованным файлом вызываем команду docker load --input vm_docker_ui.tar

Команда для запуска: docker run -d --name vm_docker_ui -p 5000:5000 vm_docker_ui

Переходим в браузере по URl http://localhost:5000

Должна появиться страница с текстом Test home page


Функционал и требования:

1. Возможность зарегистрировать нового пользователя
2. Возможность войти из под учетной записи зарегистрированного пользователя
3. По требованию, при регистрации обязательными полями являются: Email и Password, остальные поля необязательные

Описание тестового задания:

- Подготовить набор автотестов. Рекомендуемые языки: Java, C#, Python. Используемые фреймворки - любые
- Если были найдены баги, их описание необходимо также приложить к выполненному заданию (в виде любого текстового файла)
- Подготовленный набор найденных багов и автотестов необходимо выложить в ваш GitHub репозиторий и предоставить ссылку на него (Репозиторий должен быть public)