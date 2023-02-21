import discord
from discord.ext import commands

class CenturionCreateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.temp_channels = {}

    async def create_temp_channel(self, member, category):
        guild = member.guild
        channel_name = f"[🔊] {member.display_name}"
        category_id = category.id if category else None
        new_channel = await guild.create_voice_channel(channel_name, category=category)
        await member.move_to(new_channel)
        self.temp_channels[new_channel.id] = category_id

    async def delete_empty_temp_channels(self):
        for channel_id, category_id in list(self.temp_channels.items()):
            channel = self.bot.get_channel(channel_id)
            if channel is not None and channel.name.startswith("[🔊]") and len(channel.members) == 0:
                if category_id:
                    category = self.bot.get_channel(category_id)
                else:
                    category = None
                await channel.delete()
                del self.temp_channels[channel_id]

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def createvc(self, ctx):
        category = ctx.channel.category
        new_channel = await ctx.guild.create_voice_channel("Create a Channel", category=None)
        await ctx.send("Created 'Create a channel' voice channel.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await self.delete_empty_temp_channels()
        if before.channel is not None and before.channel.id in self.temp_channels and len(before.channel.members) == 0:
            category_id = self.temp_channels.pop(before.channel.id)
            if category_id:
                category = self.bot.get_channel(category_id)
            else:
                category = None
            await before.channel.delete()

        if after.channel is not None and after.channel.name.startswith("[🔊]"):
            category = after.channel.category
            if category is not None and category.id in self.temp_channels.values():
                self.temp_channels[after.channel.id] = category.id
            else:
                self.temp_channels[after.channel.id] = None

        if after.channel is not None and after.channel.name == "Create a Channel":
            category = after.channel.category
            await self.create_temp_channel(member, category)

def setup(bot):
    bot.add_cog(CenturionCreateChannel(bot))
