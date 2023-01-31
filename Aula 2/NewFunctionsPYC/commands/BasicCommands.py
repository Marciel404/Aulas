import discord
from NewFunctionsPYC import CommandPrefix, prefixContext, Slash_Command, slashContext
from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:

        self.bot = bot

        super().__init__()

    @CommandPrefix() #Command Prefix
    async def embed(self, ctx: prefixContext):
        await ctx.reply("TEste")
    
    # @Slash_Command(name = "Teste") #Slash Command Prefix
    # async def NomeSimbolico(self, interaction: slashContext):
    #     await interaction.response.send_message("TEste")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))