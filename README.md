# Recipes service
***Storage for uploading images.***

### Technologies

- Python 3.9
- Django 3.2.9
- Django Rest Framework 3.12.4

### Quick start

1. Install and activate the virtual environment
2. Install all packages from [requirements.txt](https://github.com/nick-rebrik/recipes_api/blob/main/requirements.txt)<br>
  ```pip install -r requirements.txt```
3. Run in command line:<br>
  ```python manage.py makemigrations```<br>
  ```python manage.py migrate```<br>
  ```python manage.py runserver```<br>
4.To load test data: <br>
  ```python manage.py loaddata data.json```
5. Visit the [homepage](http://127.0.0.1:8000/api) and start using
