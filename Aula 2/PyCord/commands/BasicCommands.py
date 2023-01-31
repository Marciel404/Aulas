import discord
from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:

        self.bot = bot

        super().__init__()

    @commands.command() #Command Prefix
    async def embed(self, ctx: commands.Context):
        await ctx.reply("TEste")
    
    # @Slash_Command(name = "teste") #Slash Command Prefix
    # async def NomeSimbolico(self, interaction: discord.Interaction):
    #     await interaction.response.send_message("TEste")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))