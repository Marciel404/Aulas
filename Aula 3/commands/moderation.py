import discord
from discord.ext import commands


class moderationEvents(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        print(f"Eu entrei como {self.bot.user}")
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.message):

        print(msg.content)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):

        canal = message.guild.get_channel(int(1041448270662205551))

        e = discord.Embed(title="Message deleted")
        e.add_field(name="message", value=message.content)

        await canal.send(embed=e)

    @commands.Cog.listener()
    async def on_message_edit(self, antes: discord.Message, depois: discord.Message):

        canal = antes.guild.get_channel(int(1041448270662205551))

        e = discord.Embed(title = "Mensagem editada")
        e.add_field(name="Mensagem antiga", value=antes.content)
        e.add_field(name="Mensagem nova", value=depois.content)

        await canal.send(embed=e)

def setup(bot:commands.Bot):
    bot.add_cog(moderationEvents(bot))