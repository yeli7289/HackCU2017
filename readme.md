HackCU 2017
===========

# Installation
```bash
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```
And you're good to go! Open another terminal and print this
```bash
source ./venv/bin/activate
python manage.py runserver
```
And now we have a running server at localhost:8080 with the app.
