from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

from assets.embed_msg import embed_msg


class List(commands.Cog):
    """Command to list the possible sources"""

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    @commands.slash_command(
        name="list",
        description="A list of keywords for the news cogs",
        guild_ids=debug_guilds,
    )
    async def slist(self, interaction: discord.Interaction):
        await embed_msg(
            interaction, "There is a list of possible sources :", "", "yellow", False
        )


def setup(client):
    client.add_cog(List(client))
