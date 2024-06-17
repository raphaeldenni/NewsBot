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

    # Create the bot
    activity = discord.Activity(type=discord.ActivityType.watching, name="the news")
    client = commands.Bot(intents=discord.Intents.default(), activity=activity)

    # Load commands and events
    for file in listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension("cogs." + file[:-3])

    client.run(token)


if __name__ == "__main__":
    main()
