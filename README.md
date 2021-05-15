# Treasure Hunt

Website to hunt for Pins and Passwords

## Up and Running

### Environment variables

If run on a public website the following environment variables should be set

- `DJANGO_SETTINGS_MODULE=treasurehunt.production`
- `SECRET_KEY=some_secret_key` (use a search engine to find a generator)
- `DEBUG_MODE=False` (or `True` depending on the testing state)

## Test locally

### Unix

To install everything needed for the project run the following commands.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After that the default django commands are used

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The http://127.0.0.1:8000/admin page should be used to add a question.
