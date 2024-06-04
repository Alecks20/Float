from discord.ext import commands
import discord
from src.config import bot, db
import src.libraries as libraries
import src.embeds as embeds

class core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping",description="Health check, see system ping")
    async def ping(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(colour=embeds.embed_colour, description=f"Pong! Connections take {round(bot.latency * 1000)}ms")
        await ctx.respond(embed=embed)

def setup(bot):
  bot.add_cog(core(bot))