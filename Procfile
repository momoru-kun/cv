web: python ./manage.py makemigrations; python ./manage.py migrate; gunicorn backend.wsgi:application -w 3