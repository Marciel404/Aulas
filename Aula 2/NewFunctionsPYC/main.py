import NewFunctionsPYC
import json

with open("config.json") as f:
    configData = json.load(f)

client = NewFunctionsPYC.Client(token=configData["token"],poweredby=False)

client.load_cogs("commands")

client.__run__()