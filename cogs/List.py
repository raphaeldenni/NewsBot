from assets.imports import  discord, commands, load_dotenv, getenv, embed_msg


class List(commands.Cog):

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    # List command
    @commands.slash_command(name="list", description="A list of keywords for the news cogs", guild_ids=debug_guilds)
    async def slist(self, interaction: discord.Interaction):
        await embed_msg(
            interaction,
            "There is a list of possible sources :",
            "",
            "yellow",
            False
        )


def setup(client):
    client.add_cog(List(client))
