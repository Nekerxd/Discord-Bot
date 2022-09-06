from logging import Manager
import os
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

def load_cogs(bot):
        bot.load_extension("manager")
        bot.load_extension("tasks.dates")
        bot.load_extension("commands.images")
        bot.load_extension("commands.music")
        bot.load_extension("commands.reactions")
        bot.load_extension("commands.smarts")
        bot.load_extension("commands.talks")
    
    
load_cogs(bot)

bot.run('')