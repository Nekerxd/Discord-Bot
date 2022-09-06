from discord.ext import commands

class Reactions(commands.Cog):
    """ Works with reactions """
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):  
        print(reaction.emoji)
        if reaction.emoji == "✅":
            role = user.guild.get_role(910285338113617931)
        await user.add_roles(role)
        
def setup(bot):
    bot.add_cog(Reactions(bot))