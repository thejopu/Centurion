import json
from discord.ext import commands
import os

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reaction_roles = {}
        self.load_reaction_roles()

    def load_reaction_roles(self, guild=None):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(os.path.join(dir_path, 'reaction_roles.json'), 'r') as f:
                self.reaction_roles = json.load(f)
        except FileNotFoundError:
            self.reaction_roles = {}

    def save_reaction_roles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'reaction_roles.json'), 'w') as f:
            json.dump(self.reaction_roles, f, indent=4)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id
        if guild_id is None:
            return

        guild = self.bot.get_guild(guild_id)
        if guild is None:
            return

        if str(payload.message_id) not in self.reaction_roles:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        role_id = self.reaction_roles[str(payload.message_id)].get(str(payload.emoji))
        if role_id is None:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild_id = payload.guild_id
        if guild_id is None:
            return

        guild = self.bot.get_guild(guild_id)
        if guild is None:
            return

        if str(payload.message_id) not in self.reaction_roles:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        role_id = self.reaction_roles[str(payload.message_id)].get(str(payload.emoji))
        if role_id is None:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reactionrole(self, ctx, message_id: int, emoji, role: commands.RoleConverter):
        try:
            await ctx.message.delete()
        except:
            pass

        message = await ctx.fetch_message(message_id)

        if str(message_id) not in self.reaction_roles:
            self.reaction_roles[str(message_id)] = {}

        if isinstance(emoji, str):
            if emoji.startswith('<'):
                emoji_id = int(emoji.split(':')[2][:-1])
                emoji = self.bot.get_emoji(emoji_id)
            else:
                emoji = emoji.strip(':')

        await message.add_reaction(emoji)
        self.reaction_roles[str(message_id)][str(emoji)] = role.id
        self.save_reaction_roles()

    @reactionrole.error
    async def reactionrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Invalid emoji or role. Make sure you're using custom emojis correctly and that the role exists.")

def setup(bot):
    bot.add_cog(ReactionRoles(bot))
