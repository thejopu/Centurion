import discord
from discord.ext import commands
import json
import os

class CenturionOneWordStory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_story_channels = {}

        # Get directory path of this file
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Load data from json file
        if os.path.exists(os.path.join(dir_path, 'one_word_story.json')):
            with open(os.path.join(dir_path, 'one_word_story.json'), 'r') as f:
                self.word_story_channels = json.load(f)
        else:
            with open(os.path.join(dir_path, 'one_word_story.json'), 'w') as f:
                json.dump(self.word_story_channels, f)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def onewordstory(self, ctx):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if ctx.channel.id in self.word_story_channels.values():
            await ctx.send("This channel is already a one word story channel.")
        else:
            self.word_story_channels[ctx.guild.id] = ctx.channel.id
            await ctx.send("This channel has been set up as a one word story channel.")
            with open(os.path.join(dir_path, 'one_word_story.json'), 'w') as f:
                json.dump(self.word_story_channels, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.channel.id not in self.word_story_channels.values():
            return

        if len(message.content.split()) > 1:
            await message.delete()
            return

        if message.author.id == self.bot.user.id:
            return

        last_messages = [msg async for msg in message.channel.history(limit=2)]
        if len(last_messages) == 2:
            last_author_id = last_messages[1].author.id
            if message.author.id == last_author_id:
                await message.delete()
                return


def setup(bot):
    bot.add_cog(CenturionOneWordStory(bot))
