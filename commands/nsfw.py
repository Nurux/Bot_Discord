from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup

class Nsfw(commands.Cog):
    """Comandos nsfw do bot"""
    def __init__(self, bot):
        self.bot = bot

    #Envia gif nsfw de neko
    @commands.command(name="nsfw")
    async def get_img_nsfw(self, ctx):
        try:
            response = requests.get('https://neko-love.xyz/api/v1/nekolewd')
            img = response.json()['url']
            

            msg = "uwu ~(°-°~)...(~°-°)~ uwu"

            embed = discord.Embed(
                title = msg,
                color = 0xE91E63
            )

            embed.set_image(url=img)

            await ctx.send(embed=embed)
        except Exception as error:
            await ctx.send("Ops ... \nOcorreu algum erro")
            print(error)
                

def setup(bot):
    bot.add_cog(Nsfw(bot))