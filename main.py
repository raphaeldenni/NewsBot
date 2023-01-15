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
async def embed_msg(ctx, title, message, color=0xff0000, ephemeral=True):
    embed = discord.Embed(title=title, description=message, color=color)

    await ctx.respond(embed=embed, ephemeral=ephemeral)


async def api_request(ctx, sources, keyword):
    api_key = getenv('API_KEY')

    if api_key is None:
        await embed_msg(
            ctx,
            "API key error",
            "You need to set your API key first !"
        )

        return None

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
        await embed_msg(
            ctx,
            "Connection error",
            f"Can't connect to the API ! Verify your API key and try again !\nDetail : \n{err}"
        )

        return None

    else:
        # JSON data to Python dictionary
        content = loads(req.content)

        if content['status'] == 'error' and content['code'] == 'apiKeyInvalid':
            await embed_msg(
                ctx,
                "API key error",
                "Your API key is invalid ! Verify your API key and try again !"
            )

            return None

        # Collect articles' data and send it to Discord
        total_results = str(content['totalResults'])

        return content


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


# Bot commands

# Ping command
@bot.slash_command(name="ping", description="Pong !")
async def ping(ctx):
    # Calculate the latency
    pong = round(bot.latency, 3) * 1000

    # Send the latency
    await embed_msg(
        ctx,
        "Pong ! :ping_pong:",
        f"The latency is {pong} ms",
        0xffff00,
        False
    )


# API command
@bot.slash_command(name="api", description="Set your API key")
async def api(ctx, key: discord.Option(str)):
    # Check if the key is valid
    with open(".env", "r") as f:

        for line in f.readlines():
            try:
                key = key
                name = 'API_KEY_' + str(ctx.guild_id)

                name, key = line.split('=')
                putenv(name, key)
            except ValueError:
                # syntax error
                pass

    await embed_msg(
        ctx,
        "API key set",
        f"Your API key is now set !",
        0xffff00
    )


# News command
@bot.slash_command(name="list", description="A list of keywords for the news commands")
async def slist(ctx):
    await embed_msg(
        ctx,
        "There is a list of possible sources :",
        "",
        0xffff00,
        False
    )


@bot.slash_command(name="news", description="Give fresh news")
async def news(ctx, limit: discord.Option(int), sources: discord.Option(str), keyword: discord.Option(str),
               is_list: discord.Option(bool)):
    content = await api_request(ctx, sources, keyword)

    if content is None:
        return

    if is_list is False:
        for article in content['articles']:
            if limit == 0:
                break
            elif limit > 5:
                await embed_msg(
                    ctx,
                    "Limit error",
                    "Too many articles requested ! The maximum limit is 5."
                )
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
            )
            embed \
                .set_author(name=name) \
                .set_image(url=url_to_image) \
                .set_footer(text=f"Publié par {author}")

            await ctx.respond(embed=embed)

            limit -= 1

    elif is_list is True:
        embed = discord.Embed(
            title="Fresh news !",
            color=discord.Colour.blue(),
        )

        for article in content['articles']:
            if limit == 0:
                break

            sleep(1)

            name = article['source']['name']
            title = article['title']
            description = article['description']
            published_at = article['publishedAt']

            published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

            embed.set_field_at(name=f"{title} sur {name}", value=f"{description}\nPublication: {published_at}",
                               inline=True)

        await ctx.respond(embed=embed)

    else:
        await embed_msg(
            ctx,
            "Parameter error",
            "Wrong parameter for \"is_list\". The available parameter are \"True\" or \"False\""
        )

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
