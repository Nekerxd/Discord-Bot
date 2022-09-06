import discord
from discord.ext import commands


class Talks(commands.Cog):
    """ Talks with user """
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="oi", help="O bot te da um Olá. Não é nessário utlizar Argumento")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Olá, " +name

        await ctx.send(response)

    @commands.command(name="segredo", help="Envia um segredo no seu privado. Não requer Argumento")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Não sei se você ficou sabendo")
            await ctx.author.send("Mas hoje o Guilherme")
            await ctx.author.send("TA COM O CUZINHO DANDO BOTE!!!")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções » Privacidade)")
        
def setup(bot):
    bot.add_cog(Talks(bot))