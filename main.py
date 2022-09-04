# News Bot by Raphaël DENNI aka SlyEyes

# Import
import discord

from os import getenv

from dotenv import load_dotenv

from time import sleep

from json import loads

from datetime import datetime

import requests

# Variables

load_dotenv()

token = getenv('TOKEN')

bot = discord.Bot(debug_guilds=[714560415958302780])

api_key = getenv('API_KEY')


# Bot functions


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="ping", description="Pong !")
async def ping(ctx):
    pong = round(bot.latency, 3) * 1000

    await ctx.respond(f"Pong ! ({pong} ms)")


@bot.slash_command(name="news", description="Give fresh news")
async def news(ctx, limit: discord.Option(int), sources: discord.Option(str), keyword: discord.Option(str)):

    # Request's URL
    api_url = f"https://newsapi.org/v2/everything" \
              f"?domains={sources}" \
              f"&q={keyword}" \
              f"&sortBy=publishedAt" \
              f"&sortBy=popularity" \
              f"&apiKey={api_key}"

    # Request to News API
    try:
        req = requests.get(api_url)

    except ConnectionError as err:
        print(err)
        exit()

    else:
        print("Requested content found\n")

    # JSON data to Python dictionary
    content = loads(req.content)

    # Collect articles' data and send it to Discord
    total_results = str(content['totalResults'])

    print(f"{total_results} press articles found in total")

    print(f"\nLimit set to {limit}")

    num = 1

    for article in content['articles']:
        if limit == 0:
            break

        sleep(1)

        print(f"\nArticle {num} :")

        print(article)

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
            timestamp=published_at
        )\

        embed.set_author(name=name) \
            .set_image(url=url_to_image) \
            .set_footer(text=f"Published by {author}")

        await ctx.respond(embed=embed)

        print("\nPostman here ! Article successfully delivered !")

        limit -= 1
        num += 1


bot.run(token)
