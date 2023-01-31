import NewFunctionsPYC
import json

with open("config.json") as f:
    configData = json.load(f)

client = NewFunctionsPYC.Client(token=configData["token"])

@client.command()
async def hello(ctx):
    await ctx.reply("Hello World")

client.__run__()