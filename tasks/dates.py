from discord.ext import commands, tasks
import datetime


class Dates(commands.Cog):
    """ Work with dates """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):        
        print("Estou Pronto!")
        
def setup(bot):
    bot.add_cog(Dates(bot))
