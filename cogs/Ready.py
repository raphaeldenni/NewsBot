from discord.ext import commands


class Ready(commands.Cog):
    """Event when the bot is ready"""

    client: commands.Bot = None

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"{self.client.user} is ready and online!")


def setup(client: commands.Bot) -> None:
    client.add_cog(Ready(client))
