from discord.ext import commands
import requests
import discord

color = 0xFFA500
img_binance = "https://tecnoblog.net/wp-content/uploads/2021/01/Binance.png"

class Crypto(commands.Cog):
    """Comandos de crypto moeda"""
    def __init__(self, bot):
        self.bot = bot

    #Mostra cotação atual do bitcoin segundo a API da binance
    @commands.command(name='bitcoin')
    async def cotacaobit(self, ctx):
        try:
            response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL")
            data = response.json()
            price = data.get('price')

            if price :
                price = float(price)

                embedtrue = discord.Embed(
                    title = f"1 - Bitcoin = {price: .0f} reais",
                    description = "Contação atual do bitcoin para real, disponibilizado pela API da Binance",
                    color = color
                )

                embedtrue.set_image(url=img_binance)

                await ctx.send(embed=embedtrue)

        except Exception as error:
            await ctx.send("Ops ... \nOcorreu algum erro")
            print(error)

    #Mostra cotação atual do ethereum segundo a API da binance
    @commands.command(name='ethereum')
    async def cotacaoeth(self, ctx):
        try:
            response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHBRL")
            data = response.json()
            price = data.get('price')

            if price :
                price = float(price)

                embed = discord.Embed(
                    title = f"1 - Ethereum = {price: .0f} reais",
                    description = "Cotação atual do ethereum para real, disponibilizado pela API da Binance",
                    color = color
                )

                embed.set_image(url=img_binance)

                await ctx.send(embed=embed)
        except Exception as error:
            await ctx.send("Ops ...\nOcorreu algum erro")
            print(error)


def setup(bot):
    bot.add_cog(Crypto(bot))


