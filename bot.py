import discord 
import os
import io
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='!',description="A bot made ay Antony, reviving the old SharkBot by Nico and DEAD",owner_id=382574338685009920)

@bot.event
async def on_ready():
    await ctx.send("Bot is online!")

if not os.environ.get('TOKEN'):
print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
