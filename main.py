# ======================== #
# NewsBot by Raphaël Denni #
# ======================== #

from os import getenv, listdir

import discord
from discord.ext import commands
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    token = getenv("TOKEN")

    if token is None:
        raise ValueError("No token found")

    client = commands.Bot(intents=discord.Intents.default())

    # Load commands and events
    for file in listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension("cogs." + file[:-3])

    # Update the bot's status
    client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="the news")
    )

    client.run(token)


if __name__ == "__main__":
    main()
