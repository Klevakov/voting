Приложение для проведения голосований.

Для установки приложения:
1) создайте и активируйте виртуальное окружение в выбранной дирректории;
2) в терминале перейдите в дирректорию проекта;
3) выполните команду "pip install -r requirements.txt" для установки необходимых пакетов и библиотек;
4) в терминале перейдите в каталог /mysite/;
5) выполните команду "manage.py makemigrations voting";
6) выполните команду "manage.py migrate";
7) для запуска приложения выполните команду "manage.py runserver".

Приложение станет доступно по адресу: http://127.0.0.1:8000/

Алгоритм работы приложения, а также схема структуры базы данных представлены в файле "Voting.pdf" 
