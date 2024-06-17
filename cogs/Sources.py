from os import getenv

from discord.ext import commands
from dotenv import load_dotenv
from newsapi import NewsApiClient
from json import loads

from assets.send_message import send_message


class Sources(commands.Cog):
    """Command to list the possible sources"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    @commands.slash_command(
        name="sources",
        description="A list of possible sources",
        guild_ids=debug_guilds,
    )
    async def sources(self, interaction) -> None:
        api = NewsApiClient(api_key=getenv("NEWSAPI_KEY"))

        try:
            sources_request = api.get_sources()

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

        if sources_request["status"] != "ok":
            await send_message(
                interaction,
                "No sources list found",
                "",
                "info",
                is_ephemeral=True,
            )

        raw_sources = sources_request["sources"]

        sources = ""

        for source in raw_sources:
            source_id = source["id"]
            source_name = source["name"]

            sources += f"{source_name} ({source_id})\n"

        await send_message(
            interaction,
            "Here is a list of possible sources [NAME (ID TO USE)]:",
            sources,
            is_ephemeral=True,
        )


def setup(client: commands.Bot) -> None:
    client.add_cog(Sources(client))
