import discord
from newsapi import NewsApiClient

from os import getenv
from dotenv import load_dotenv
from json import loads
from time import sleep
from datetime import datetime

from assets.send_message import send_message


class News(discord.Cog):
    """Command to get the news"""

    # Initialize the bot
    bot: discord.Bot = None

    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    # Define the slash command
    slash_command_kwargs = {
        "name": "news",
        "description": "Get the latest news",
    }

    # Add the guild_ids if in debug mode
    load_dotenv()
    debug_guild = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    if debug_guild:
        slash_command_kwargs["guild_ids"] = debug_guild

    # News command
    @discord.slash_command(**slash_command_kwargs)
    async def news(
        self,
        interaction,
        sources: discord.Option(str),
        keyword: discord.Option(str),
        limit: discord.Option(int),
    ) -> None:
        # Get the news trough the News API
        api = NewsApiClient(api_key=getenv("NEWSAPI_KEY"))

        try:
            news_response = api.get_everything(q=keyword, sources=sources)

        except Exception as e:
            error_message = loads(e)["message"]

            await send_message(
                interaction,
                "Error",
                error_message,
                "error",
                is_ephemeral=True,
            )

            return

        if news_response is None:
            await send_message(
                interaction,
                "No articles found",
                f"No articles found for the keyword '{keyword}' and/or source(s) '{sources}'.",
                "info",
                is_ephemeral=True,
            )

            return

        # Get the articles and decompose them to a embed Discord message
        articles = news_response["articles"]

        for article in articles:
            if limit == 0:
                break

            elif limit > 5:
                await send_message(
                    interaction,
                    "Limit error",
                    "Too many articles requested ! The maximum limit is 5.",
                    "error",
                    is_ephemeral=True,
                )

                break

            sleep(1)

            source = article["source"]["name"]
            author = article["author"]
            title = article["title"]
            description = article["description"]
            link = article["url"]
            photo = article["urlToImage"]
            raw_timestamp = article["publishedAt"]

            timestamp = datetime.strptime(raw_timestamp, "%Y-%m-%dT%H:%M:%SZ")

            if author is None:
                author = source

            embed = (
                discord.Embed(
                    title=title,
                    url=link,
                    description=description,
                    timestamp=timestamp,
                    color=0xFFFF00,
                )
                .set_author(name=source)
                .set_image(url=photo)
                .set_footer(text=f"Published by {author}")
            )

            await interaction.response.send_message(embed=embed)

            limit -= 1


def setup(bot: discord.Bot) -> None:
    bot.add_cog(News(bot))
