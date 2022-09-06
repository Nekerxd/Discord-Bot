import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Se junta ao chat de voz que o usuário está")
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"Você precisa estar em um canal de voz!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_cliet.move_to(voice_channel)
    
    @commands.command(help="Disconecta do chat de voz atual")
    async def dc(self,ctx):
        await ctx.voice_client.disconnect()
        
    @commands.command(aliases=["p"], help="Da play em uma música do Youtube. Requer Argumentos: url")
    async def play(self,ctx,url):
        embed = discord.Embed(title=f"Música iniciada ⏯", description=f"URL: {url}", color=discord.Color.red())
        await ctx.send(embed=embed)
        ctx.voice_client.stop()
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            vc.play(source)
        
    @commands.command(help="Pausa a música que está sendo reproduzida")
    async def pause(self,ctx):
        embed = discord.Embed(title=f"Música pausada ⏸", color=discord.Color.red())
        embed.set_footer(text=f"Música pausada por {ctx.author.mention}")
        await ctx.send(embed=embed)
        await ctx.voice_client.pause()
        
    @commands.command(help="Retoma a música que foi pausada")
    async def resume(self,ctx):
        embed = discord.Embed(title=f"Música retomada ▶", color=discord.Color.red())
        embed.set_footer(text=f"Música retomada por {ctx.author.mention}")
        await ctx.send(embed=embed)
        await ctx.voice_client.resume()
    
def setup(bot):
    bot.add_cog(Music(bot))
