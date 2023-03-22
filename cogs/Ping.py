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

"""
   Copyright 2022-2023 Raphaël Denni

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
