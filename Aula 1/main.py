import discord
import NewFunctionsPYC
import json
from discord.ext.commands import Bot

with open("config.json") as f:
    configData = json.load(f)

#Usando NewFunctionsPYC
client = NewFunctionsPYC.Client(token=configData["token"])

@client.command()
async def hello(ctx):
    await ctx.reply("Hello World")

client.__run__()


#Usando pycord
client = Bot(command_prefix = "!", intents = discord.Intents.all())

@client.command()
async def hello(ctx):
    await ctx.reply("Hello World")

client.run(configData["token"])
