# Treasure Hunt

Website to hunt for Pins and Passwords

## Up and Running

### Environment variables

If run on a public website the following environment variables should be set

- DJANGO_SETTINGS_MODULE=treasurehunt.production
- SECRET_KEY=some_secret_key (use a search engine to find a generator)
- DEBUG_MODE=False (or True depending on the testing state)

## Test locally

Unix

```
python3 -m venv venv
source venv/bin
```
