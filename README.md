# ChatBot_REST_API

cd ChatBot_REST_API

pip install virtualenv

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

Python3 manage.py runserver

The API url path is http://127.0.0.1:8000/api/schema/docs/.

I use Swagger for API documentation.


I use a simple SQLite database but you can change it to Postgresql database. You can just create your PostgreSQL database in pgAdmin and change the DATABASE in setting.py.

