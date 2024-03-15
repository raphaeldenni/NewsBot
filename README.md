# NewsBot

A bot to use the [News API]("https://newsapi.org/") in Discord !

## Requirements

The following modules are required:

- Pycord (2.0.0 or above)
- python-dotenv (latest)
- Requests (latest)

All of them are listed in `pyproject.toml` and `requirements.txt`

You also need to provide 2 variables in a `.env` file:

- `TOKEN` : a Discord's bot token
- `API_KEY` : an api key from [News API]("https://newsapi.org/")

## Installation

Don't forget to use Poetry integrated environments or venv with pip

### Poetry (Recommended)

```sh
poetry install
```

### Pip

```sh
pip install -r requirements.txt
```
