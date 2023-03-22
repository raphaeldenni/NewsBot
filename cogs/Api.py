from assets.imports import discord, commands, load_dotenv, getenv, putenv, embed_msg


class Api(commands.Cog):

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    # API command
    @commands.slash_command(name="api", description="Set your API key", guild_ids=debug_guilds)
    async def api(self, interaction: discord.Interaction, key: discord.Option(str)):
        # Check if the key is valid
        with open(".env", "r") as f:

            for line in f.readlines():
                try:
                    key = key
                    name = 'API_KEY_' + str(interaction.guild_id)

                    name, key = line.split('=')
                    putenv(name, key)
                except ValueError:
                    # syntax error
                    pass

        await embed_msg(
            interaction,
            "API key set",
            f"Your API key is now set !",
            "yellow"
        )


def setup(client):
    client.add_cog(Api(client))
