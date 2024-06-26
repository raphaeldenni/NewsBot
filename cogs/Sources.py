import discord
from newsapi import NewsApiClient

from os import getenv
from dotenv import load_dotenv
from json import loads

from assets.send_message import send_message


class Sources(discord.Cog):
    """Command to list the possible sources"""

    # Initialize the bot
    bot: discord.Bot = None

    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    # Define the slash command
    slash_command_kwargs = {
        "name": "sources",
        "description": "List of possible sources",
    }

    # Add the guild_ids if in debug mode
    load_dotenv()
    debug_guild = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    if debug_guild:
        slash_command_kwargs["guild_ids"] = debug_guild

    # Sources command
    @discord.slash_command(**slash_command_kwargs)
    async def sources(self, interaction) -> None:
        # Get the sources trough the News API
        api = NewsApiClient(api_key=getenv("NEWSAPI_KEY"))

        try:
            sources_response = api.get_sources()

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

        if sources_response["status"] != "ok":
            await send_message(
                interaction,
                "No sources list found",
                "",
                "info",
                is_ephemeral=True,
            )

        # Format the sources and send them
        raw_sources = sources_response["sources"]

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


def setup(bot: discord.Bot) -> None:
    bot.add_cog(Sources(bot))
