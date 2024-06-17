from datetime import datetime
from os import getenv
from time import sleep
from json import loads

import discord
from discord.ext import commands
from dotenv import load_dotenv
from newsapi import NewsApiClient

from assets.send_message import send_message


class News(commands.Cog):
    """Command to get the news"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    # News command
    @commands.slash_command(
        name="news",
        description="Give fresh news",
        guild_ids=debug_guilds,
    )
    async def news(
        self,
        interaction,
        sources: discord.Option(str),
        keyword: discord.Option(str),
        limit: discord.Option(int),
    ) -> None:
        api = NewsApiClient(api_key=getenv("NEWS_API_KEY"))

        try:
            articles = api.get_everything(q=keyword, sources=sources)

        except Exception as e:
            error_message = loads(e)["message"]

            print(error_message)

            await send_message(
                interaction,
                "Error",
                error_message,
                "error",
                is_ephemeral=True,
            )

            return

        if articles is None:
            await send_message(
                interaction,
                "No articles found",
                "No articles found for this keyword and/or source.",
                "info",
                is_ephemeral=True,
            )

            return

        for article in articles["articles"]:
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

            name = article["source"]["name"]
            author = article["author"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            url_to_image = article["urlToImage"]
            published_at = article["publishedAt"]

            published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

            if author is None:
                author = name

            embed = discord.Embed(
                title=title,
                url=url,
                description=description,
                timestamp=published_at,
                color=0xFFFF00,
            )
            embed.set_author(name=name).set_image(url=url_to_image).set_footer(
                text=f"Published by {author}"
            )

            await interaction.response.send_message(embed=embed)

            limit -= 1


def setup(client: commands.Bot) -> None:
    client.add_cog(News(client))
