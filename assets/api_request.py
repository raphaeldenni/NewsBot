from json import loads
from os import getenv

import discord
import requests

from assets.send_message import send_message


async def api_request(
    interaction: discord.Interaction, sources: str, keyword: str
) -> dict:
    """Request to News API

    Args:
        interaction (discord.Interaction): The interaction object
        sources (str): The sources of the news
        keyword (str): The keyword to search

    Returns:
        dict: The articles' data
    """
    api_key = getenv("API_KEY")

    if api_key is None:
        await send_message(
            interaction,
            "API key error",
            "You need to set your API key first !",
            "error",
            is_ephemeral=True,
        )

        return None

    # Request's URL
    api_url = (
        f"https://newsapi.org/v2/everything"
        f"?domains={sources}"
        f"&q={keyword}"
        f"&sortBy=publishedAt"
        f"&sortBy=popularity"
        f"&apiKey={api_key}"
    )

    # Request to News API
    try:
        req = requests.get(api_url)

    except ConnectionError as err:
        await send_message(
            interaction,
            "Connection error",
            f"Can't connect to the API ! Verify your API key and try again !\nDetail : \n{err}",
            "error",
            is_ephemeral=True,
        )

        return None

    else:
        # JSON data to Python dictionary
        content = loads(req.content)

        if content["status"] == "error" and content["code"] == "apiKeyInvalid":
            await send_message(
                interaction,
                "API key error",
                "Your API key is invalid ! Verify your API key and try again !",
                "error",
                is_ephemeral=True,
            )

            return None

        # Collect articles' data and send it to Discord
        total_results = str(content["totalResults"])

        return content
