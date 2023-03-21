# News Bot by Raphaël DENNI aka SlyEyes

# Import
from  assets.imports  import  *

# Variables
load_dotenv()

token = getenv('TOKEN')

bot = discord.Bot(debug_guilds=[714560415958302780])

embed_list = discord.Embed(
            title="Fresh news !",
            color=0x0000ff,
        )

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
async def news(ctx, limit: discord.Option(int), sources: discord.Option(str), keyword: discord.Option(str)):
    content = await api_request(ctx, sources, keyword)

    if content is None:
        return

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
