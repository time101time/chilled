import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.event
async def on_ready():
    print("BOT ON")
    print("*------*")


@client.command()
async def test(ctx):
    await ctx.send("TEST COMPLETE! IF YOU READ THIS THE BOT IS WORKING! CONGRATULATIONS!")

client.run('TOKEN')
