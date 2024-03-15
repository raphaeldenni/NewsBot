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
        importance (str, optional): The importance of the message. Defaults to "normal".
        is_ephemeral (bool, optional): If the message is ephemeral. Defaults to False.
    """
    match importance:
        case "error":
            color = 0xFF0000  # Red
        case "info":
            color = 0xFFFF00  # Yellow
        case "normal":
            color = 0x00FF00  # Green

    embed_msg = discord.Embed(title, message, color)

    await interaction.response.send_message(embed_msg, is_ephemeral)
