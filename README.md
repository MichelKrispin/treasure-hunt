# Treasure Hunt

A Website to hunt for pins and passwords.

There are questions which can be written on an admin site and if the stream of questions are correctly answered by a user a pin or password will be presented.

(Great for someone who should work a little by answering a few questions before receiving the Wifi password)

## Up and Running

### Environment variables

If run on a public website the following environment variables should be set

- `DJANGO_SETTINGS_MODULE=treasurehunt.production`
- `SECRET_KEY=some_secret_key` (use a search engine to find a generator)
- `DEBUG_MODE=False` (or `True` depending on the testing state)

There might be an issue with the migrations. If there is an error at the index page `python manage.py makemigrations hunting` and then `python manage.py migrate` might solve the problem.

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

## Admin site

There are two models: The `map` and the `stage`. A stage is one question with a corresponding answer. Each map is the top level structure which holds the secret password and starts the first stage (that one with the lowest level).

On each stage the answer will be checked and if correct the next stage with the next higher level will be linked. The latest (highest level) question will not show the question but only a pre-written text and the maps password.
