from discord.ext import commands
import discord

class Help(commands.Cog):
    """Lista todos os comandos do bot"""
    def __init__(self, bot):
        self.bot = bot

    #Lista todos os comandos do bot
    @commands.command(name='ajuda')
    async def list_comands(self, ctx):

        embed = discord.Embed(
            title = '**Lista de comandos**',
            description = '--------------------\n**Interação**\n--------------------' + 
                          '\nhug = mostra gif de abraço\nkiss = mostra gif de beijo\ncute = mostra gif fofinho\n' +
                          'uwu = simplismente uwu\nalarm = mostra gif de acordar\nbaka = mostra gif falando baka\nbat = mostra gif batendo\n\n' + 
                          '--------------------\n**NSFW**\n--------------------' + 
                          '\nnsfw = mostra img nsfw de neko\n\n' +
                          '--------------------\n**Crypto**\n--------------------' +
                          '\nbitcoin = mostra cotação atual do bitcoin\nethereum = mostra a contação atual do ethereum',
            color = 0XE74C3C
        )

        await ctx.send(embed=embed)
                

def setup(bot):
    bot.add_cog(Help(bot))