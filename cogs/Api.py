from os import getenv, putenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

from assets.send_message import send_message

# NOTE: Not secure and doesn't work, think to delete this command


class Api(commands.Cog):
    """Command to set the API key"""

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    @commands.slash_command(
        name="api",
        description="Set your API key",
        guild_ids=debug_guilds,
    )
    async def api(self, interaction: discord.Interaction, key: discord.Option(str)):
        # Check if the key is valid
        with open(".env", "r") as f:
            for line in f.readlines():
                try:
                    key = key
                    name = "API_KEY_" + str(interaction.guild_id)

                    name, key = line.split("=")
                    putenv(name, key)
                except ValueError:
                    # syntax error
                    pass

        await send_message(
            interaction,
            "API key set",
            "Your API key is now set !",
            "yellow",
            is_ephemeral=True,
        )


def setup(client):
    client.add_cog(Api(client))
