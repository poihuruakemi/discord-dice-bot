from keep_alive import keep_alive

keep_alive()  # これで Flask が別スレッドで動く

import discord
from discord.ext import commands
import re
import time
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def prng(seed):
    return (seed * 1103515245 + 12345) % (2**31)

@bot.event
async def on_ready():
    print("Botが起動しました")

@bot.command()
async def dice(ctx, dice):
    match = re.fullmatch(r'(\d*)d(\d+)', dice)
    if not match:
        await ctx.send("NdM形式（例: d2, 4d5）で入力してね")
        return

    n = int(match.group(1)) if match.group(1) else 1
    m = int(match.group(2))

    seed = int(time.time() * 1000) ^ ctx.author.id

    rolls = []
    for _ in range(n):
        seed = prng(seed)
        rolls.append(seed % m + 1)

    await ctx.send(f"🎲 {n}d{m} → {rolls} 合計: {sum(rolls)}")

bot.run(os.environ["BOT_TOKEN"])


