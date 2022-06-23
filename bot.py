from discord.ext import commands
from decouple import config 
import os

bot = commands.Bot('!')

bot.load_extension("manager")
bot.load_extension("tasks.Dates")

for file in os.listdir("./commands"):
    if file.endswith(".py"):
        cog = file[0:-3]
        bot.load_extension(f"commands.{cog}")


TOKEN = config("Token")
bot.run(TOKEN)

