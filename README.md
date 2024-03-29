# NewsBot

A bot to use the [News API]("https://newsapi.org/") in Discord !

## Requirements

The following modules are required:

- py-cord (^2.4.1)
- python-dotenv (^1.0.0)
- requests (^2.31.0)

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
