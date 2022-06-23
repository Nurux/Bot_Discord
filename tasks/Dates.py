from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """Taks de horas"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(seconds=60)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y ás %H:%M:%S")
        channel = self.bot.get_channel(900814152518483978)

        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))