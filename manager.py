from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Manager(commands.Cog):
    """ Manage the bot """
    
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
    print(f"Estou pronto! Estou conectado como {self.bot.user}")
    #current_time.start() #Descomentar para ativar a task
    
#@commands.Cog.listener()
async def on_message(self, message):
    if message.author == self.bot.user:
        return
    
    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!"
        )
        
        await message.delete()
    
    await self.bot.process_commands(self, message)


@commands.Cog.listener()
async def on_command_error(self, ctx, error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send("É necessário utilizar todos Argumentos. Em caso de dúvidas, digite >help para ver os parâmetros de cada comando")
    elif isinstance(error,CommandNotFound):
        await ctx.send("**Este não é um comando válido! nEm caso de dúvidas, digite >help para ver todos os comandos**")
    else:
        raise error
 
def setup(bot):
    bot.add_cog(Manager(bot))
