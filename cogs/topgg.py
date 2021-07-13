import dbl
import discord
from discord.ext import commands
from postgres import Bot


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = '' # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True, webhook_path="/dblwebhook",webhook_port=5000, webhook_auth="") # Autopost will post your guild count every 30 minutes

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Server count posted successfully")


    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        print(f"Received a test upvote: {data}")
        userid = int(data['user'])
	
        await Bot.addvoted(self, userid , "True")

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        print(f"Received a test upvote: {data}")
        userid = int(data['user'])
	
        await Bot.addvoted(self, userid , "True")


def setup(bot):
    bot.add_cog(TopGG(bot))