from assets.imports import *


async def embed_msg(interaction, title, message, color, ephemeral=True):
    if color == "red":
        color = 0xff0000
    elif color == "yellow":
        color = 0xffff00
    else:
        color = 0x00ff00

    embed = discord.Embed(title=title, description=message, color=color)

    await interaction.response.send_message(embed=embed, ephemeral=ephemeral)

    """
       Copyright 2022 Raphaël Denni

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
