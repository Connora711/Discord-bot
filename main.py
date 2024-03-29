import discord
from discord.ext import commands
import random

# This is the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# This is the bot commands
# Says hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Tells ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# Repeats the message
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Gives a random number
@bot.command()
async def number(ctx):
    await ctx.send(random.randint(1, 100))

# Feel good
@bot.command()
async def look(ctx):
    await ctx.send('You look good!')

# Bot token
bot.run('your token here')
