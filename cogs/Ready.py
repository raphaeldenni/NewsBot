from assets.imports import *


class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user} is ready and online!")


def setup(client):
    client.add_cog(Ready(client))
