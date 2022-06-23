from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class Dates(commands.Cog):
    """Manager bot"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto!\nConectado com {self.bot.user}')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando não existente.\nDigite !ajuda para ver a lista de comandos")
        else:
            raise error


def setup(bot):
    bot.add_cog(Dates(bot))