import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import main
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "test":
        all = Moppen.query.all()
        randomint = random.randint(1, len(all))
        print(randomint)
        text = Moppen.query.all()[randomint - 1]
        text = str(text)
        text = text.split(",")
        embed=discord.Embed(title="Mop " + str(randomint), description=str(text[0]), color=0x00ff40)
        embed.set_footer(text=text[1])
        await client.send_message(message.channel, embed=embed)

def run():
    client.run("code")
