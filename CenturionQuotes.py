import discord
import random
from discord.ext import commands

class CenturionQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Define a list of quotes with their corresponding authors and images
        self.quotes = [
            {
                "text": "I bloody love a good smoothie. It's all the pleasure of eating without the hassle of chewing.",
                "author": "Grumio",
                "image": "https://i.imgur.com/tu6SR5r.png"
            },
            {
                "text": "It's your tunic, so technically, I'm pissing yourself.",
                "author": "Marcus Phillipus Valerius Gallo",
                "image": "https://i.imgur.com/yPEvKtl.png"
            },
            {
                "text": "It's Water Man.",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            },
            {
                "text": "No that's a threesome, two guys can't be a gang can they.",
                "author": "Stylax Rufus Eurisces",
                "image": "https://i.imgur.com/wP7mddn.png"
            },
            {
                "text": "I saw you earlier, with the.. hairy stick.",
                "author": "Grumio",
                "image": "https://i.imgur.com/tu6SR5r.png"
            },
            {
                "text": "Do you think it's possible I give herpes to a cat?",
                "author": "Stylax Rufus Eurisces",
                "image": "https://i.imgur.com/wP7mddn.png"
            },
            {
                "text": "Flavia! Flavia! There's a fucking hand in the jug!",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            },
            {
                "text": "You're knobbing your cousin, because it's the closest you can get to having sex with yourself.",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            },
            {
                "text": "Dirty dirty dirty dick, you've got a dirty dick. Urghhhh cousin fucker",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            },
            {
                "text": "His penis could have eaten my penis for breakfast.",
                "author": "Marcus Phillipus Valerius Gallo",
                "image": "https://i.imgur.com/yPEvKtl.png"
            },  
            {
                "text": "No actually, on their knees worshipping my rack.",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            }, 
            {
                "text": "I DO NOT HAVE BOOBS!",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            },  
            {
                "text": "Will you come in with me? Incase the doctor tries to finger me.",
                "author": "Stylax Rufus Eurisces",
                "image": "https://i.imgur.com/wP7mddn.png"
            }, 
            {
                "text": "My name is Stylax, I'm into weird sex, I shag my granny, in her fanny, I kiss my brother, I fuck my mother, and all my uncles 🎵🎵.",
                "author": "Aurelius aka. Water Man*",
                "image": "https://i.imgur.com/UwU6t7Q.png"
            }    
        ]

    @commands.command(name="quote")
    async def quote(self, ctx):
        # Pick a random quote from the list
        quote = random.choice(self.quotes)

        # Create an embed with the quote text and author
        embed = discord.Embed(title="Random Quote", description=quote["text"], color=0xe91234)
        embed.set_footer(text=f"- {quote['author']}")
        

        # Set the thumbnail to the image of the author
        embed.set_thumbnail(url=quote["image"])

        # Send the embed as a message
        message = f"{ctx.author.mention} here's your quote! <:quote:1076922518193053746>"
        await ctx.send(message)
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(CenturionQuotes(bot))
