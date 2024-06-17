from os import getenv

from discord.ext import commands
from dotenv import load_dotenv
from newsapi import NewsApiClient

from assets.send_message import send_message


class List(commands.Cog):
    """Command to list the possible sources"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    @commands.slash_command(
        name="list",
        description="A list of keywords for the news cogs",
        guild_ids=debug_guilds,
    )
    async def slist(self, interaction) -> None:
        api = NewsApiClient(api_key=getenv("NEWS_API_KEY"))

        sources = api.get_sources()

        print(sources)

        await send_message(
            interaction,
            "Here a list of possible sources :",
            sources["sources"],
            is_ephemeral=True,
        )


def setup(client: commands.Bot) -> None:
    client.add_cog(List(client))
