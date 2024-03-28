python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

start python manage.py runserver

start python manage.py bot