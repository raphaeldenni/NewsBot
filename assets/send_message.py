import discord


async def send_message(
    interaction: discord.Interaction,
    title: str,
    message: str,
    importance: str = "normal",
    is_ephemeral: bool = False,
) -> None:
    """Send an embed message to Discord

    Args:
        interaction (discord.Interaction): The interaction object
        title (str): The title of the embed message
        message (str): The content of the embed message
        importance (str, optional): The importance of the message. Can be "error", "info" or "normal". Defaults to "normal".
        is_ephemeral (bool, optional): If the message is ephemeral. Defaults to False.
    """
    match importance:
        case "normal":
            color = discord.Color.blue()
        case "info":
            color = discord.Color.yellow()
        case "error":
            color = discord.Color.red()
        case _:
            color = discord.Color.default()

    embed_message = discord.Embed(title=title, description=message, color=color)

    await interaction.response.send_message(embed=embed_message, ephemeral=is_ephemeral)
