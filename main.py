# ======================== #
# NewsBot by Raphaël Denni #
# ======================== #

from os import getenv, listdir

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    token = getenv("TOKEN")

    if token is None:
        raise ValueError("No token found")

    client = commands.Bot(intents=Intents.default())

    # Load commands
    for file in listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension("cogs." + file[:-3])

    client.run(token)


if __name__ == "__main__":
    main()
