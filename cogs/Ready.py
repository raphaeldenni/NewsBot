import discord


class Ready(discord.Cog):
    """Event when the bot is ready"""

    bot: discord.Bot = None

    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print(f"{self.bot.user} online and ready!")


def setup(bot: discord.Bot) -> None:
    bot.add_cog(Ready(bot))
