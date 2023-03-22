from assets.imports import discord, commands, load_dotenv, getenv, embed_msg


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    # Ping command
    @commands.slash_command(name="ping", description="Pong !", guild_ids=debug_guilds)
    async def ping(self, interaction: discord.Interaction):
        # Calculate the latency
        pong = round(self.client.latency, 3) * 1000

        # Send the latency
        await embed_msg(
            interaction,
            "Pong ! :ping_pong:",
            f"The latency is {pong} ms",
            "yellow",
            False
        )


def setup(client):
    client.add_cog(Ping(client))
