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

# Choose a suitable LLM and explain why I chose this LLM.

For hosting a local language model (LLM), you would typically consider factors such as model size, performance, resource requirements, and ease of integration. Also it's Open-source that can be used and modified without licensing fees and 
performance which provides a good balance between performance and resource requirements.


