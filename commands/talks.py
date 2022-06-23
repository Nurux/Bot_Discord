from discord.ext.commands.core import command
from discord.ext import commands
import discord
import kawaiiapi

file = open('commands/imgAPI.env')
token_img_api = file.read()

color = 0x00D166

class Talks(commands.Cog):
    """Comandos de interação com o usuário"""
    def __init__(self, bot):
        self.bot = bot

    #Envia um gif de abraço
    @commands.command(name='hug')
    async def get_gif_hug(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "hug")

        embed = discord.Embed(
            title = 'Tó um babaço :3',
            color = color
        )

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif de beijo
    @commands.command(name='kiss')
    async def get_gif_kiss(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "kiss")

        embed = discord.Embed(
            title = 'Beijinho uwu',
            color = color
        )

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif fofo
    @commands.command(name='cute')
    async def get_gif_cute(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "cute")

        embed = discord.Embed(
            title = "Fofinho vc...\n...vc fofinho owo",
            color = color
        )

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif uwu
    @commands.command(name='uwu')
    async def get_gif_uwu(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "uwu")

        embed = discord.Embed(
            title = "Simplismente uwu",
            color = color
        )

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif de acordar
    @commands.command(name='alarm')
    async def get_gif_alarm(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "alarm") 

        embed = discord.Embed(
            title = "Bom dia...",
            color = color
        ) 

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif baka
    @commands.command(name='baka')
    async def get_gif_baka(self, ctx):
        api = kawaiiapi.Kawaii(token_img_api)
        await api.endpoints("gif")
        img = await api.get("gif", "baka")

        embed = discord.Embed(
            title = "Baka *****^*****",
            color = color
        )

        embed.set_image(url=img)

        await ctx.send(embed=embed)

    #Envia gif batendo
    @commands.command(name="bat")
    async def get_img_sla(self, ctx):
        url_img = "https://c.tenor.com/Z2J0XHsTCJYAAAAC/kuroko-kick-ass.gif"
        msg = '***Toma seu arrombado!***\n'

        embed = discord.Embed(
            color = color
        )

        embed.set_image(url=url_img)

        await ctx.send(msg, embed=embed)


def setup(bot):
    bot.add_cog(Talks(bot))
