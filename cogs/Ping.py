import discord

from os import getenv
from dotenv import load_dotenv

from assets.send_message import send_message


class Ping(discord.Cog):
    """Command to ping the bot"""

    # Initialize the bot
    bot: discord.Bot = None

    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    # Define the slash command
    slash_command_kwargs = {
        "name": "ping",
        "description": "Pong!",
    }

    # Add the guild_ids if in debug mode
    load_dotenv()
    debug_guild = [int(getenv("DEBUG_GUILD"))] if getenv("DEBUG_GUILD") else []

    if debug_guild:
        slash_command_kwargs["guild_ids"] = debug_guild

    # Ping command
    @discord.slash_command(**slash_command_kwargs)
    async def ping(self, interaction) -> None:
        # Calculate the latency
        latency = round(self.bot.latency, 3) * 1000

        # Send the latency
        await send_message(
            interaction,
            "Pong! :ping_pong:",
            f"{latency} ms of latency",
        )


def setup(bot: discord.Bot) -> None:
    bot.add_cog(Ping(bot))
