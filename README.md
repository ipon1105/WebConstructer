# WebConstructer
 
Веб-Конструктор с множеством функционала.


Чтобы запустить сборку фронта в первый раз нужно выполнить команду cd vue
После запустить установку npm install
Далее можно собирать проект командой npm run serve

Что бы запустить django необходимо запуситить pgAdmin 4
После этого надо будет в файле setting.py добавить базу, пользователя и пароль

После этого необходимо провесит миграции
python -m manage makemigrations
python -m manage migrate

Для запуска сервера
python -m manage runserver 0.0.0.0:8000

Если у вас не запускается, докачайте необходимые модули