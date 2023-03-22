import discord

from assets.imports import *


class News(commands.Cog):

    def __init__(self, client):
        self.client = client

    load_dotenv()
    debug_guilds = [int(getenv("DEBUG_GUILD"))]

    # News command
    @commands.slash_command(name="news", description="Give fresh news", guild_ids=debug_guilds)
    async def news(self, interaction: discord.Interaction, limit: discord.Option(int), sources: discord.Option(str),
                   keyword: discord.Option(str)):
        content = await api_request(interaction, sources, keyword)

        if content is None:
            return

        for article in content['articles']:
            if limit == 0:
                break
            elif limit > 5:
                await embed_msg(
                    interaction,
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

            await interaction.response.send_message(embed=embed)

            limit -= 1


def setup(client):
    client.add_cog(News(client))
