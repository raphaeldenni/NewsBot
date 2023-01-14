# News_Bot
A bot to use the News API in Discord !

## Requirements

You need to install the following Python module with pip : 
- Pycord (2.0.0 or above) : `python -m pip install py-cord`
- python-dotenv (latest) : `python -m pip install python-dotenv`
- Requests (latest) : `python -m pip install requests`

You also need to provide 2 variables :
- `token` : a Discord's bot token
- `api_key` : an api key from <a href="https://newsapi.org/">News API</a>

You can store the variables above-mentioned into a `.env` file with the following format :
```dotenv
TOKEN=[your_token]
API_KEY=[your_api_key]
```
