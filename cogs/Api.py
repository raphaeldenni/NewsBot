# from os import getenv, putenv

from discord.ext import commands

# from dotenv import load_dotenv
from assets.send_message import send_message

# NOTE: Not secure and doesn't work, think to delete this command


class Api(commands.Cog):
    """Command to set the API key"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    #    load_dotenv()
    #    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    @commands.slash_command(
        #        name="api",
        #        description="Set your API key",
        #        guild_ids=debug_guilds,
    )
    async def api(self, interaction) -> None:
        # , key: discord.Option(str)):
        # Check if the key is valid
        await send_message(
            interaction,
            "Obsolete command",
            "This command is not secure and doesn't work. Please use the .env file instead.",
            "error",
            is_ephemeral=True,
        )


#        with open(".env", "r") as f:
#            for line in f.readlines():
#                try:
#                    key = key
#                    name = "API_KEY_" + str(interaction.guild_id)
#
#                    name, key = line.split("=")
#                    putenv(name, key)
#                except ValueError:
#                    # syntax error
#                    pass
#
#        await send_message(
#            interaction,
#            "API key set",
#            "Your API key is now set !",
#            "info",
#            is_ephemeral=True,
#        )


def setup(client: commands.Bot) -> None:
    client.add_cog(Api(client))
