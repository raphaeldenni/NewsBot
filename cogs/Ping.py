from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

from assets.send_message import send_message


class Ping(commands.Cog):
    """Command to ping the bot"""

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    @commands.slash_command(
        name="ping",
        description="Pong !",
        guild_ids=debug_guilds,
    )
    async def ping(
        self,
        interaction: discord.Interaction,
    ):
        # Calculate the latency
        pong = round(self.client.latency, 3) * 1000

        # Send the latency
        await send_message(
            interaction,
            "Pong ! :ping_pong:",
            f"There is {pong} ms of latency",
            "yellow",
        )


def setup(client):
    client.add_cog(Ping(client))
