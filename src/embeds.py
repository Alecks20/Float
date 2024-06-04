import discord
import traceback
from src.config import db, bot
import src.libraries as libraries

embed_colour = 0x404D67

def get(primary, category, content):
  try:

    if primary == "core":
      if category == "update":
        title = content[0]
        description = content[1]
        interaction = content[2]
        embed = discord.Embed(title=title, description=description, colour=embed_colour)
        embed.set_author(name=interaction.user.name.capitalize() + "・Bot Developer", icon_url=interaction.user.avatar)
        embed.set_footer(text=interaction.guild.name)
      if category == "error":
        embed = discord.Embed(colour=embed_colour,description=f"Uh oh! An error occured, thankfully it was caught by our handler. If this error continues report it to our support server```{content}```")
      if category == "simple":
        embed = discord.Embed(colour=embed_colour,description=content)
      if category == "denied":
        embed = discord.Embed(colour=0xff3939,description=f"<:offline:1078291224840114186> {content}")
      if category == "success":
        embed = discord.Embed(colour=0x1fff8b,description=f"<:online:1078291279756136488>  {content}")

    if primary == "fun":
      if category == "ows":
        if content[0] == "reset":
            embed = discord.Embed(colour=embed_colour, title="Story has been reset!", description="The story has been reset, all of the words in the story have been cleared from the active story cache")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
            embed.set_footer(text=f"Requested by {content[1].name.capitalize()}",icon_url=content[1].avatar)
        
        elif content[0] == "welcome":
            embed = discord.Embed(colour=embed_colour, title="Welcome to the One Word Story!", description="This channel has been configured as the one word story channel, you can't send more than 1 message in a row and you can't have more than 1 word in a message")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
            embed.set_footer(text=f"Requested by {content[2].name.capitalize()}",icon_url=content[2].avatar)
        
        elif content[0] == "disabled":
            embed = discord.Embed(colour=embed_colour, title="One word story disabled", description="The one word story channel has been disabled and has been reset, all data has been cleared from our system")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
            embed.set_footer(text=f"Requested by {content[2].name.capitalize()}",icon_url=content[2].avatar)
        
        elif content[0] == "log":
            embed = discord.Embed(colour=embed_colour, title=f"Message Deleted in one word stories",description=content[1])
            embed.add_field(name="Deletion Reason", value=content[5])
            embed.set_author(name=f"Original Message by {content[2]}" , icon_url=content[3])
            embed.set_footer(text=content[4])
        
        elif content[0] == "logs set":
            embed = discord.Embed(colour=embed_colour, title=f"Logs channel set",description="This channel has been configured as the logs channel for one word stories")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content[0] == "compile":
            embed = discord.Embed(colour=embed_colour, title="Your one word story", description=content[1])
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content == "published":
            embed = discord.Embed(colour=embed_colour, title="One word story published", description="The previous story has been published to your servers library, the story in this channel has been automatically reset")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content == "limit":
            embed = discord.Embed(colour=embed_colour, title="Length Limit", description="That word will take your story over the 4096 chracter limit (Discords embed description limit) Either publish/reset your story or send a different word")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content == "halfway-warning":
            embed = discord.Embed(colour=embed_colour, title="Length warning", description="You have gone over the halfway mark on how long your story can be, think about publishing/restting it soon")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content == "nearly-at-limit":
            embed = discord.Embed(colour=embed_colour, title="Length warning", description="You are 96 characters off the one word story character limit, you should REALLY think about publishing/restting your story")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
        
        elif content[0] == "purged":
            embed = discord.Embed(colour=embed_colour, title="Channel Purged", description=f"The one word story channel was just purged having {content[1]} message(s) purged from the channel and the story, if anything is missing thats why")
            embed.add_field(name="Social Links",value=libraries.SOCIAL_LINKS,inline=False)
            embed.set_footer(text=f"Purged by {content[2].name.capitalize()}",icon_url=content[2].avatar)


    return embed

  except Exception:
      embed = get("core","error",traceback.format_exc())
      return embed