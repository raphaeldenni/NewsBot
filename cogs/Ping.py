from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

from assets.send_message import send_message


class Ping(commands.Cog):
    """Command to ping the bot"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    @commands.slash_command(
        name="ping",
        description="Pong !",
        guild_ids=debug_guilds,
    )
    async def ping(self, interaction: discord.Interaction) -> None:
        # Calculate the latency
        latency = round(self.client.latency, 3) * 1000

        # Send the latency
        await send_message(
            interaction,
            "Pong ! :ping_pong:",
            f"{latency} ms of latency",
        )


def setup(client: commands.Bot) -> None:
    client.add_cog(Ping(client))
