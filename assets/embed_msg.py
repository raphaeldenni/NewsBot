import discord


async def embed_msg(
    interaction: discord.Interaction,
    title: str,
    message: str,
    color_choice: str = "",
    is_ephemeral: bool = True,
) -> None:
    """Send an embed message to Discord

    Args:
        interaction (discord.Interaction): The interaction object
        title (str): The title of the embed message
        message (str): The content of the embed message
        color_choice (str): The color of the embed message
        is_ephemeral (bool, optional): If the message is ephemeral. Defaults to True.
    """
    match color_choice:
        case "red":
            color = 0xFF0000
        case "yellow":
            color = 0xFFFF00
        case _:
            color = 0x00FF00

    embed_msg = discord.Embed(title, message, color)

    await interaction.response.send_message(embed_msg, is_ephemeral)
