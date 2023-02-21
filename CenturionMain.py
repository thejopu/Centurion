import discord
from discord.ext import commands
from CenturionQuotes import CenturionQuotes
from CenturionReactionRoles import ReactionRoles
from CenturionCreateChannel import CenturionCreateChannel
from CenturionOneWordStory import CenturionOneWordStory



# Enable all intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    cogs_to_load = [
        CenturionQuotes(bot),
        ReactionRoles(bot),
        CenturionCreateChannel(bot),
        CenturionOneWordStory(bot),
       
        
    ]
    for cog in cogs_to_load:
        await bot.add_cog(cog)
        if isinstance(cog, ReactionRoles):
            for guild in bot.guilds:
                cog.load_reaction_roles(bot)
        
        
       

    

   

   






bot.run('MTA3NjkxOTQ0NTk0OTI1OTg2OA.Gb-esd.cm2WSOEt0Vdqy3oQ99vWhrdcUgZntzy3oCByME')