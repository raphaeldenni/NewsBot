# News Bot by Raphaël DENNI aka SlyEyes

# Import
import discord

from os import getenv, putenv

from dotenv import load_dotenv

from time import sleep

from json import loads

from datetime import datetime

import requests

# Variables
load_dotenv()

token = getenv('TOKEN')

bot = discord.Bot(debug_guilds=[714560415958302780])

# Functions
def encrypt_api_key(api_key, guild_id):
    return api_key

def decrypt_api_key(api_key, guild_id):
    return api_key

async def error_embed(ctx, title, message, color=0xff0000):
    embed = discord.Embed(title=title, description=message, color=color)
    await ctx.respond(embed=embed, ephemeral=True)
    return

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


# Bot functions

# Ping command
@bot.slash_command(name="ping", description="Pong !")
async def ping(ctx):
    # Calculate the latency
    pong = round(bot.latency, 3) * 1000

    # Send the latency
    embed = discord.Embed(
        title="Pong ! :ping_pong:",
        description=f"The latency is {pong} ms",
        color=0xffff00
    )

    await ctx.respond(embed=embed)


# API command
@bot.slash_command(name="api", description="Set your API key")
async def api(ctx, key: discord.Option(str)):
    # Check if the key is valid
    with open(".env", "r") as f:

        for line in f.readlines():
            try:
                key = encrypt_api_key(key, str(ctx.guild_id))
                name = 'API_KEY_' + str(ctx.guild_id)

                name, key = line.split('=')
                putenv(name, key)
            except ValueError:
                # syntax error
                pass

    embed = discord.Embed(
        title="API key set",
        description=f"Your API key is now set !",
        color=0xffff00
    )

    await ctx.respond(embed=embed, ephemeral=True)

# News command
@bot.slash_command(name="news", description="Give fresh news")
async def news(ctx, limit: discord.Option(int), sources: discord.Option(str), keyword: discord.Option(str)):
    api_key = decrypt_api_key(getenv(f'API_KEY_{ctx.guild.id}'), str(ctx.guild_id))

    if api_key is None:
        await error_embed\
                (
                    ctx,
                    "API key error",
                    "You need to set your API key first !"
                )
        return

    # Request's URL
    api_url = \
        f"https://newsapi.org/v2/everything" \
        f"?domains={sources}" \
        f"&q={keyword}" \
        f"&sortBy=publishedAt" \
        f"&sortBy=popularity" \
        f"&apiKey={api_key}"

    # Request to News API
    try:
        req = requests.get(api_url)

    except ConnectionError as err:
        await error_embed\
            (
                ctx,
                "Connection error",
                "Connection to the API failed ! Verify your API key and try again !"
                f"\n\nDetails : \n{err}"
            )
        exit()

    else:
        # JSON data to Python dictionary
        content = loads(req.content)

        if content['status'] == 'error' and content['code'] == 'apiKeyInvalid':
            await error_embed\
                (
                    ctx,
                    "API key error",
                    "Your API key is invalid ! Verify your API key and try again !"
                )
            return

        # Collect articles' data and send it to Discord
        total_results = str(content['totalResults'])

        for article in content['articles']:
            if limit == 0:
                break

            sleep(1)

            name = article['source']['name']
            author = article['author']
            title = article['title']
            description = article['description']
            url = article['url']
            url_to_image = article['urlToImage']
            published_at = article['publishedAt']

            published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

            if author is None:
                author = name

            embed = discord.Embed(
                title=title,
                url=url,
                description=description,
                timestamp=published_at,
                color=0xffff00
            )\

            embed.set_author(name=name) \
                .set_image(url=url_to_image) \
                .set_footer(text=f"Published by {author}")

            await ctx.respond(embed=embed)

            limit -= 1

bot.run(token)


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
