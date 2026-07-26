import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

with open("config.json", "r") as f:
    config = json.load(f)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("✅ Namma Kadai Promotion Bot is Online!")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != config["source_channel"]:
        return

    for channel_id in config["target_channels"]:
        channel = client.get_channel(channel_id)

        if channel:
            if message.content:
                await channel.send(message.content)

            for attachment in message.attachments:
                await channel.send(attachment.url)

client.run(TOKEN)