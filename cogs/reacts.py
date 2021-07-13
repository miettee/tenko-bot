from discord.ext import commands
import discord
import os
import sys
import pickle

class reacts(commands.Cog):



    def __init__(self, bot):
        self.bot = bot
        self.stop_dict = {}
        self.stopp = {}

        self.state_file = "/root/tenko/state/tog state.txt"
        # your text file that stores people's toggles ( all the other stuff is in a database , i didnt add this one bc it works fine for wahts needed)

    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")
        sys.stdout.flush()

    def writeState(self):
        try:
            with open(self.state_file,'wb') as f:
 
                pickle.dump((self.stopp),f,protocol=pickle.HIGHEST_PROTOCOL)
        except:
            pass

    def readState(self):
        with open(self.state_file, 'rb') as f:
            try:
                self.stopp = pickle.load(f)
            except:
                self.stopp = {}

    @commands.command(name='reacttoggle', aliases=["rt", "toggle"])
    async def reacttoggle(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        self.readState()
        serverid = ctx.message.guild.id
        channelid = ctx.message.channel.id

        if serverid not in self.stopp:
            self.stopp.update({serverid : []})
            self.stopp[serverid].append(channelid)
            await ctx.send(f"Alright! I've turned *off* all my reacts for this channel, **{ctx.channel.name}**!")
            self.writeState()
            pass
        else:
            if channelid in self.stopp[serverid]:

                self.stopp[serverid].remove(channelid)
                self.writeState()
                await ctx.send(f"Alright! I've turned back *on* all my reacts for this channel, **{ctx.channel.name}**!")
            else:
                self.stopp[serverid].append(channelid)
                self.writeState()
                await ctx.send(f"Alright! I've turned *off* all my reacts for this channel, **{ctx.channel.name}**!")

    def check_toggle(self, serverid, channelid):
        if serverid not in self.stopp:
            return False
        else:
            if channelid in self.stopp[serverid]:
                return True
            else:
                return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        emoji_map = {('women', 'lady', 'girl') : '👍', ('men', 'angie', 'yonaga', 'korekiyo') : '😠',
                     ('himiko', 'yumeno', 'lesbian') : '🥰',('seesaw', 'shotput', 'piranhas', 'ritual') : '😳',
                     ('girl in red', 'sweater weather', 'neo aikido') : '💓' }

        # every word and react ^-^

        try:
            for tupe, moji in emoji_map.items():
                if any(i in message.content.lower().split() for i in tupe):
                    channelid = message.channel.id
                    serverid = message.guild.id
                    self.readState()
                    if not self.check_toggle(serverid, channelid):
                        await message.add_reaction(moji)
        except discord.Forbidden:
            pass

def setup(bot):
    bot.add_cog(reacts(bot))