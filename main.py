# ======================== #
# NewsBot by Raphaël Denni #
# ======================== #

import discord
from dotenv import load_dotenv
from os import getenv, listdir


def main() -> None:
    load_dotenv()
    token = getenv("BOT_TOKEN")

    if token is None:
        raise ValueError(
            "No Discord app token found, please add a .env file with the BOT_TOKEN variable"
        )

    # Create the bot
    activity = discord.Activity(type=discord.ActivityType.watching, name="the news")
    bot = discord.Bot(intents=discord.Intents.default(), activity=activity)

    # Load commands and events
    for file in listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension("cogs." + file[:-3])

    bot.run(token)


if __name__ == "__main__":
    main()
