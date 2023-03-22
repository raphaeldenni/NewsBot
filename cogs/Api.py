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
