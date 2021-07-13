from discord.ext import commands
import discord

import sys
import datetime

import traceback
import io
import time
import math
import asyncio
import random
from colorthief import ColorThief
from postgres import Bot

#this is all the economy stuff


class vibecheck2(commands.Cog):
    def __init__(self, bot):
        self.cooldown_map = {}
        self.stop_set = set()

        self.dangans = ['Makoto', 'Sayaka', 'Leon', 'Kyoko', 'Byakuya',
                'Mondo', 'Toko', 'Celestia', 'Aoi', 'Kiyotaka',
                'Sakura', 'Yasuhiro', 'Chihiro', 'Mukuro',

                'Hajime', 'Gundham', 'Kazuichi',
                'Nekomaru', 'Fuyuhiko', 'Akane', 'Chiaki',
                'Sonia', 'Hiyoko',
                'Mahiru', 'Mikan',
                'Ibuki', 'Peko',
                'Angie', 'Gonta',
                'Himiko', 'Kaede', 'Kaito', 'Kiibo',
                'Kirumi',
                'Korekiyo', 'Maki', 'Miu', 'Rantaro', 'Ryoma', 'Shuichi','Tsumugi']

        self.bot = bot

    async def return_values(self, id):
        shorten = await Bot.query(self, id)

        if shorten is None:
            await Bot.add(self,id)
            shorten = await Bot.query(self, id, 0,0,0)

        shorten = list(shorten)
        shorten.remove(shorten[0])

        return shorten

    async def return_values_time(self, userid):
        shorten = await Bot.querytime(self, userid)

        shorten = list(shorten)
        shorten.remove(shorten[0])

        return shorten


    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")


    async def is_cooldown_time(self, userid, type):
        now = time.time()
        ctime = 0
        if type == "vibe":
            ctime = 43200
            placeorder=0
        if type == "ask":
            ctime = 14400
            placeorder = 1


        if await Bot.querytime(self, userid):
            times = await self.return_values_time(userid)
            timi = times[placeorder]

            cooldowntime = timi + ctime

            if now > cooldowntime:
                await Bot.updatetime(self, userid, type, now)
                return (True, 0)
            else:
                return (False, cooldowntime - now)

        else:
            await Bot.addtotimes(self, userid)
            await Bot.updatetime(self, userid, type, now)
            return (True, 0)


    def roundit(self, cooldown):
        new = math.ceil(cooldown)
        new = math.ceil(new / 60)
        h, m = divmod(new, 60)
        return f"{h}h {m}m"

    def colour(self, determiner):
        colours = ["red", "green", "blue", "orange", "purple", "yellow", "turquoise", "pink", "lilac", "cream",
                   "maroon", "violet", "lime",
                   "cyan", "dark blue", "mint", "grey", "azure", "peach", "amber", "navy", "teal", "coral", "indigo", "pastel", "neon yellow",
                   "neon pink", "light pink", "grey-blue", "neon orange", "rainbow", "lemon yellow", "aquamarine", "silver", "gold"]
        if determiner:
            possibles = [f"If I had to put a colour to your vibe, I think I'd go with {random.choice(colours)}!!",

                     f"Aha!! Your vibes would definitely be {random.choice(colours)} coloured!! Amazing!!",
                     f"I'm not sure why, but your vibes would definitely be {random.choice(colours)} coloured!! I can really see it!",
                     f"If your vibes were a colour.. I think they'd be {random.choice(colours)}!! Maybe?"]
        else:
            possibles = [f"If I had to put a colour to your vibe, I think I'd go with {random.choice(colours)}?",
                         f"Hmmmm.. I think the best colour for your vibes is {random.choice(colours)}, maybe?",
                         f"These vibes feel..... {random.choice(colours)} coloured?? Maybe??"]
        return random.choice(possibles)

    def animal(self, determiner):
        animals = ["zebra", "rabbit", "dog", "cat", "mouse", "tiger", "goose", "duck", "frog", "sheep", "gecko", "bird", "worm", "ant", "ferret"]
        animals_plural = ["zebras", "rabbits", "dogs", "cats", "mice", "tigers", "giraffes", "geese", "ducks",
                          "lizards", "frogs", ]
        if determiner:
            possibles = [f"A good animal to go with your vibe... how about a {random.choice(animals)}??",
                     f"Oh!! And!! If your vibe was an animal, it would definitely be a {random.choice(animals)}!!"]
        else:
            possibles = [f"Your vibes feel like they'd go with an animal.... maybe a {random.choice(animals)}?",
                         f"An animal that would go with your vibe... probably a {random.choice(animals)}!"]
        return random.choice(possibles)

    def number(self, determiner):
        numb = random.randint(1, 100)
        if determiner:
            possibles = [f"Ooh! Your lucky vibe number is probably {numb}!!",
                     f"Wow, your vibe number is definitely {numb}!! That's a great number!!",
                     f"I'd say a great number to go with your vibe is {numb}!! I love it!!"]
        else:
            possibles = [f"Ohh.. a number that would work with your vibe would probably be {numb}!!",
                         f"I think the best number for your vibe would be {numb}!"]
        return random.choice(possibles)

    def chara(self, determiner):
        bad = random.choice(['Junko', 'Nagito', 'Kokichi', 'Monaca'])
        good = random.choice(self.dangans)
        if determiner:
            possibles = [f"I'm absolutely sure {good} would love your vibes! You should be friends!",
                         f"Wow!! These vibes are a lot like {good}'s vibes!! That's really cool!!",
                         f"These vibes remind me of {good}! I wonder why!",
                         f"I bet you know {good}- you have practically matching vibes!!",
                         f"Oh wow!! These vibes are very similar to {good}'s too!!! Amazing!"]
            return random.choice(possibles)
        else:
            possibles = [f"These vibes are very similar to {bad}'s vibes.....",
                         f'Uhhh, do you know {bad}? Ha, I bet you two\'d be best friends!! Which is not a compliment!',
                         f"Wow, your vibes are scarily close to vibes {bad} would have!!!"]
            return random.choice(possibles)

    @commands.command()
    async def vibes(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        secondoption = ['Miku', 'Himiko appreciation', 'motivation', 'Neo-Aikido', 'heart']

        #vibe checks and how many points they give you

        allvibe = {"...not the best?!?!":0,
        " lacking motivation...":-2,
        "... haha, you're joking, right? These vibes are awful!":-7,
        " sickening!!!! Are you some sort of degenerate??!":-10,
        f"... bleh!! They make me sick!! Have you tried having some {random.choice(secondoption)} in your life??":-6,
        " really bad! Sorry!!!":-8,
        "... just, not good. Really not good.":-5,
        " uuugghghgh.. I'm allergic to really bad vibes...":-10,
        " bad! So very bad!!! Aaahh!!!":-8,
        " frightening!!":0,
        " despairing.... oh..":-15,
        " very uninspiring, sadly!!":0,
        ".... kinda bad!! Aw!! I thought you'd have better vibes than this!!!!":-3,
        " very very very bad!! You should work on that!!!":0,
        " honestly!! Awful!! But don't worry, you can still improve them!! I believe in you!!":-4,
        " irredeemable!! If I'm being honest!":-8,
                   " bad!! They taste even worse... not that I would know that!!!": -10,
                   " terrible!! You need to be more positive, geez!!": -5,
                   " something I'd expect from that purple haired guy!! Don't make me say his name..": -20,
                   " bad! That's it!": -5,
                   " bottom of the barrel!! Yu can do better than this, come on!!": -7,
                   " bad bad bad!!": -5,
                   " good- ha!! I was joking!!! They're bad.": -2,
                   " ............. ........ I think?? You can tell for yourself?? How awful these vibes are?": -25,
                   " incredibly bad!! Come do Neo-Aikido with me, it's the only cure!!": -5,
                   " ... how many degenerate males have you been hanging out with lately!! You need to send them flying before it's too late for your vibe!!!": -15,
        "... vibes a degenerate male would have!!! That's awful!":-20,
        " some of the worst vibes I've seen! And I've seen a lot of vibes!!":-5,
        " the sort of vibes I'd punt across a room!!!":-6,
        " not the worst, but close!!":-1,
" pretty good!":5,
        " the best I've ever seen!":10,
        "... WOW!! HAVE YOU BEEN WORKING ON YOUR VIBES LATELY? INCREDIBLE!!!":20,
        " just fine!":9,
        " full of promise!":10,
        "... WOOHOO!! I'M LOVING THESE VIBES!!!! FANTASTIC!!!":10,
        "... wowie!! These vibes are one of a kind!! ":8,
        " pretty fine!":8,
        " good!!":7,
        "... FANTASTIC!! ALMOST AS GOOD AT HIMIKO'S MAGIC!!!! I'M AMAZED AND AWED!!!":25,
        " kinda cool!":15,
        " lovely! These vibes are top form!":15,
        " delicious!! If they were a cold beverage, I'd totally buy one!":10,
        " magical!! Himiko said that, so it's definitely true!!":15,
        " strange and unusual! How spooky!":10,
        " wild and untamed! How cool!":10,
        " sweet and sugary! How nice!":10,
        " hot and spicy! How funky!":7,
        " cool and refreshing! How... cool!!":7,
        " simple and neat! How lovely!":6,
        " truly a sight to behold!! They amaze me!!!!":12,
        " dark and mysterious! How interesting!":15,
                   " really fun!!":5,
                   " super, super cool!!": 10,
                   " really strong!! They make me want to work harder!!!": 15,
                   " quite... sad?? Bittersweet? They remind me of something...": 15,
                   " like a fruit!! Sweet and tangy!! ": 12,
                   " really passionate!!! Wow, you must be really motivated!!!": 15,
                   " very cute!! Aaah, I love cute things!!!": 17,
                   " really really cute!!! I love cute things so much!!": 20,
         " like a celebrity?!! Wait, should I be paying you to look at your vibes??": 13,
         " like an idol's!! You'll remember me when you're famous, won't you??": 10,
        " like a world cass chef's!! Delicious!! ... Not that I'd eat your vibes!!!!": 10,

        "... just like someone who practices Neo-Aikido daily! Good job, we need more vibes like these!!!":20,
        " super duper ultra amazingly magical!! I'm quoting Himiko, could you tell?":30,
        " super unique! You totally rock those vibes!! really hopeful!! They're really inspiring, wow!!":50,
        "... WOOAAHH!! I didn't know you could even have vibes this cool!! Please teach me how!?":30,
        "... the sort of vibes I'm sure Himiko would have!! That's amazing!!!":40,
        " INCREDIBLE!! THESE VIBES ARE SO AMAZING.. I DON'T KNOW WHAT TO SAY??!?":30,
        " really dazzling!!":20,
        " sparkling and bright!!!":20,

        " interesting! They made me think!!":10,
        "...average?!?!":10,
        " passable. To help, you could always add some Neo-Aikido!":10,
        "... well, you're on the right path!":10,
        " interesting! They remind me of something.. but I can't remember!":10,
        "... eh...":10,
        " hmmmm..mm...m.... alright!":10,
                   " incredibly average!! That's impressive!!": 10,
                   " nothing very special!!": 10,
                   " fine! Almost didn't notice them!": 10,
                   " quite.. underwhelming...": 10,
                   " not far off being interesting!! Really!!": 10,
                   " ok??! Come on, I don't want to rate boring vibes!!": 10,
        " neither good or bad?!! But the only way to go is up!!! ":10,
        " almost there..? Like.. really close?! To being good???":10,
        " mediocre! But that's ok! ":10,
        "... unreadable! I'll give you a pass this time though, so don't worry!":10,
        " vibes unlike any I've ever seen!! Is that a compliment? I do not know!!!!":10,
        " bland and flavourless! Like water soup! But I bet you could make it work somehow!!":10,
        " weird! You're bending time and space with those vibes!! I like them but please.. stop now.":10,
        "... oh, they make me hungry! I'm gonna go eat! Try your vibes again later?.":10,
        " honestly, not the worse!":10,
        "... uhh... Well, those are definitely vibes!! That's... good??":10,
        " a little bit like mine!!! Huh?!!":10,}


        starts = ["Hmm, well, ", "Umm.. hmmmm... ", "Hmm... ", "Hmm, umm, ", "Hmm hmm hmm, ", "Oh!! Well, ", "Well, I think that "]



        (cooldown_ok,cooldown_time) = await self.is_cooldown_time(ctx.message.author.id, "vibe")

        cooldown = self.roundit(cooldown_time)

        query = await Bot.query(self, ctx.author.id)



        if not cooldown_ok:
            if not query:
                await Bot.add(self, ctx.author.id, 1, 0, 0)
                return await ctx.send(
                    f"You don't have any vibe resets! Either wait {cooldown}, or go find some vibe resets!")

            shorten = await self.return_values(ctx.author.id)

            if shorten[2] <= 0:
                return await ctx.send(
                    f"You don't have any vibe resets! Either wait {cooldown}, or go find some vibe resets!")

            shorten[2] -= 1
            await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])

        name = ctx.message.author.name
        mention = ctx.message.author.mention

        filelink = ctx.message.author.avatar_url_as(format = "png")

        imported = io.BytesIO(await filelink.read())

        h = ColorThief(imported)
        h = h.get_color(quality=1)

        colorr = '%02x%02x%02x' % h

        colorr = int(f"0x{colorr}", base = 16)


        the_vibe = (random.choice(list(allvibe.items())))
        actual_vibe = the_vibe[0]
        vibepoints = the_vibe[1]


        if vibepoints <=0:
            dt = False
        else:
            dt = True

        extra = [self.colour(dt), self.animal(dt), self.number(dt), self.chara(dt)]


        #database things
        if not await Bot.query(self, ctx.author.id):
            await Bot.add(self,ctx.author.id, 1, vibepoints, 0)
        else:
            shorten = await self.return_values(ctx.author.id)

            shorten[0]+= 1
            shorten[1]+=vibepoints

            await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])

        luckyvibe = random.randint(1, 1000000)


        if luckyvibe == 696969:
            #im VERY funny
            actual_vibe = " **INCREDIBLY RARE**???? WHAT?? THESE.. THESE ARE ONE IN A MILLION VIBES???!!? HOW?????....???!!???"
            extra = ["Wow..... I'm still pretty shocked!!"]
            vibepoints = 200

        ms = discord.Embed(
            description=f"{random.choice(starts)}{mention}, your vibes are{actual_vibe}"
                        f"\n\n{random.choice(extra)}\n\nFor those vibes, you get {vibepoints} vibe points!!",
            colour= colorr
        )
        ms.set_author(name=f"A probably accurate vibe check for {name}!")
        ms.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.send(embed = ms)

    @commands.command()
    async def vprofile(self, ctx):

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        if not await Bot.query(self, ctx.author.id):
            shorten = [0,0,0]
            await Bot.add(self, ctx.author.id, 0, 0, 0)
        else:
            shorten = await self.return_values(ctx.author.id)

        gettext = await Bot.querycustom(self, ctx.author.id)

        if not gettext:
            c_top = "*Put your custom top text here!*"
            c_bottom = "*Put your custom bottom text here!*"
        else:
            gettext = dict(gettext)
            c_top= gettext['toptext']
            c_bottom = gettext['bottomtext']
        ms = discord.Embed(
            description=f"{c_top}\n\n"
            f"Total vibes = {shorten[0]}\n"
                        f"Vibe points = {shorten[1]}\n"
                        f"Vibe resets available = {shorten[2]}",
            colour=0x7cd081
        )
        ms.set_author(name=f"{ctx.author.name}'s vibe profile!")
        ms.set_thumbnail(url=ctx.author.avatar_url)
        ms.timestamp = datetime.datetime.utcnow()
        ms.set_footer(text=f"{c_bottom} ")
        await ctx.send(embed=ms)

    @commands.command()
    async def ask(self, ctx, *, args):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        (cooldown_ok, cooldown_time) = await self.is_cooldown_time(ctx.message.author.id, "ask")

        cooldown = self.roundit(cooldown_time)

        if not cooldown_ok:
            return await ctx.send(f"Hey!! I can't have you asking me all the time, can I?? Wait {cooldown}, geez.")

        plea = args
        odds = 10
        bonus_odds = 0
        thinking = ["Hmmm...", "Agghh... This is hard!!", "Hmm!!! Hmmm.....", "I think..... hmm hmmmm....", "Well...."]


        good_args = ["himiko", "neo aikido", "girl", "lesbian", "woman", "yumeno", "kaede"]
        bad_args = ["men", "man", "korekiyo", "angie"]

        for e in good_args:
            if e in plea:
                bonus_odds -= 3

        for e in bad_args:
            if e in plea.split(" "):
                bonus_odds += 3

        if bonus_odds <= -9:
            bonus_odds = -9

        odds = odds + bonus_odds

        randy = random.randint(1,odds)


        mesg = await ctx.send("Hmm... Let me think about it!!!")

        await asyncio.sleep(3)

        await mesg.edit(content = random.choice(thinking))

        await asyncio.sleep(4)

        if randy ==1:
            if odds > 10:
                await mesg.edit(content = "**🎉 ||** Ughh... I really hate that ask!!.... But you put it in such a good way!! I have to give you this **+1** vibe reset!!!")
            elif odds == 10:
                await mesg.edit(content = f"**🎉 ||** Well, that was an a-ok ask!! Have this **+1** vibe reset!!")
            else:
                await mesg.edit(content = "**🎉 ||** Wow!!! You really have a way with words!!! Please have this **+1** vibe reset!!")

            shorten = await self.return_values(ctx.author.id)
            shorten[2] =+1
            await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])

        else:
            if odds >10:
                await mesg.edit(content = "**❌ ||** I really really hated your ask!!! It was the worst thing I've ever heard!! So definitely not!!")
            elif odds ==10:
                await mesg.edit(content = "**❌ ||** Your ask was ok!! But it's a no this time!! Sorry!")
            else:
                await mesg.edit(content = "**❌ ||** I really liked that ask!! But it's a no this time!! Sorry!")

    @ask.error
    async def ask_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Hey!! What's your ask going to be?? If I like it, I'm way more likely to give you a vibe reset!!!")

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command()
    @commands.cooldown(1, 1200, commands.BucketType.user)
    async def rps(self, ctx, arg):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        possibles = ["rock", "paper", "scissors"]

        choice = random.choice(possibles)

        chance = random.randint(1,3)

        if chance == 3:
            amount = random.randint(1, 10)
        else:
            amount = random.randint(1, 4)


        if arg == "rock":
            if choice == "paper":
                return await ctx.send("**🪨 <- 📝 ||** Haha!! I crushed your **rock** with my mighty **paper**!!... Somehow??")
            elif choice == "rock":
                return await ctx.send("**🪨 oo 🪨 ||** We both chose **rock**!! Nothing happened!! ")
            elif choice == "scissors":

                await ctx.send(f"**🪨 -> ✂ ||** Your **rock** crushed my **scissors**!!... Well, I guess you can have **{amount} vibe points** for that, but I'll beat you next time!!")
                shorten = await self.return_values(ctx.author.id)
                shorten[1] += amount
                await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])
                return

        elif arg == "paper":
            if choice == "paper":
                return await ctx.send("**📝 oo 📝 ||** We both chose **paper**!! Nothing happened!!")
            elif choice == "rock":

                await ctx.send(f"**📝 <- 🪨 ||** Your **paper** crushed my **rock**!!... Well, I guess you can have **{amount} vibe points** for that, but you won't win next time!!")
                shorten = await self.return_values(ctx.author.id)
                shorten[1] += amount
                await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])
                return
            elif choice == "scissors":
                return await ctx.send(f"**📝 -> ✂ ||** Haha!! I cut up your **paper** into very small pieces with my **scissors**!! Take that!")

        elif arg == "scissors":
            if choice == "paper":

                await ctx.send(
                    f"**✂ <- 📝 ||** Your **scissors** crushed my **paper**!!... Well, I guess you can have **{amount} vibe points** for that, but you won't win next time!!")
                shorten = await self.return_values(ctx.author.id)
                shorten[1] += amount
                await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])
                return
            elif choice == "rock":
                return await ctx.send(f"**✂ -> 🪨 ||** Haha!! I smashed up your **scissors** with my **rock**!! Take that!")
            elif choice == "scissors":
                return await ctx.send(f"**✂ oo ✂ ||** We both chose **scissors**!! Nothing happened!!")
        else:
            return await ctx.send("Hey!! You need to choose rock, paper or scissors, otherwise we can't play!")

    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f'Hey!! You need to choose rock, paper or scissors, otherwise we can\'t play!')
        elif isinstance(error, commands.CommandOnCooldown):
            mins = self.roundit(error.retry_after)[3:]
            mins = mins[:-1]
            minu = "minutes"
            if mins == 1:
                minu = "minute"
            await ctx.send(
                f'If you want to play me for vibe points, wait {mins} {minu}!!')

            ctx.command.reset_cooldown(ctx)

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command()
    async def leaderboard(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        people, points = await Bot.order(self)

        alltop = ""

        emoji_dict = {1:"🌟 ",2:"🥈",3:"🥉",4:"✨", 5:"✨", 6:"✨", 7:"✨", 8:"✨", 9:"✨", 10:"✨"}
        for i in range (0, len(people)):
            name = await self.bot.fetch_user(people[i])
            emoji = emoji_dict[i+1]

            alltop += f"{emoji} | **#{i +1}**: {name} with {points[i]} points\n"

        ms = discord.Embed(
            description=f"{alltop}",
            colour=0xa5eecc
        )
        ms.set_author(name=f"Vibe Leaderboard")


        ms.set_thumbnail(url="https://64.media.tumblr.com/6f8aeda64fa2087ae0c29b012b23c2de/tumblr_pcabv9kGjj1u8ndlho3_500.png")
        await ctx.send(embed=ms)

    @commands.command()
    async def vote(self, ctx):

        #nb : this bit will not work without being added on top.gg

        status = await Bot.checkvoted(self,ctx.author.id)

        ms = discord.Embed(
            description=f"You can vote [here](https://top.gg/bot/663427713654325278/vote) every 12 hours on top.gg!\nFor your vote, you'll get **+2 vibe resets** and some **vibe points**!!\nOnce you've voted, run this command again!",
            colour=0x0a8049
        )
        ms.set_author(name=f"⭐ Voting!")
        ms.set_thumbnail(url="https://64.media.tumblr.com/bf1e2284233ad9b771eb206237127007/tumblr_p6wt3gKEn21wck85po3_1280.jpg")

        if not status:
            await ctx.send(embed=ms)

            await Bot.addvoted(self, ctx.author.id, "False")
            return

        status = dict(status)

        status = status["voted"]

        if status == "False":
            await ctx.send(embed=ms)
        else:
            amount = random.randint(20,30)
            ms.description=f"Thank you for your vote!! You now have **+2** vibe resets and **+{amount}** vibe points!!"
            ms.set_author(name=f"🌟 Thank you!")
            ms.set_thumbnail(url = "https://64.media.tumblr.com/0ec1de146c27f3b60a78ffdf40f724f7/tumblr_pcabv9kGjj1u8ndlho8_500.png")
            await ctx.send(embed=ms)

            shorten = await self.return_values(ctx.author.id)
            shorten[1] += amount
            shorten[2] += 2
            await Bot.update(self, ctx.author.id, shorten[0], shorten[1], shorten[2])
            await Bot.addvoted(self,ctx.author.id, "False")

    @commands.command()
    async def voteydaubee(self, ctx):
        await Bot.addvoted(self,ctx.author.id, "True")


    @commands.command()
    async def vibecoms(self,ctx):

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        eg = discord.Embed(

            description='All of these commands are based around vibe points! Earn points and vibe resets, play minigames, and compete with others to become the best viber ever!!' \
                        '\n \n» **Vibe Point Commands:**' \
                        '\n`vibes` - Check your current vibes, and gain or lose vibe points! You can freely vibe check every 12 hours, or use a vibe reset!' \
                        '\n`ask *your ask*` - Ask me nicely for a vibe reset every 4 hours!! If I like your response, I\'m a lot more likely to give you one!' \
                        '\n`rps *your play*` - Play rock paper scissors against me for vibe points every 20 minutes!' \
                        '\n`vote` - Vote to gain two resets and some vibe points! Run the command again after your vote to get your rewards!' 
                        '\n \n» **Other Commands:**' \
                        '\n`vprofile` - See all your vibe data- points, resets and times vibed!' \
                        '\n`tcustom` - Customise the top text of your vprofile!' \
                        '\n`bcustom` - Customise the bottom text of your vprofile!' \
                        '\n`leaderboard` - See the current top 10 vibers!' ,


            colour=0xb6e2a6

        )

        eg.set_author(name='Vibe Economy Commands')
        eg.set_thumbnail(
            url='https://64.media.tumblr.com/6d473a0c3d9067f8013f9f147d0326f8/tumblr_p6wt3gKEn21wck85po5_1280.jpg')
        await ctx.message.channel.send(embed=eg)

    @commands.command()
    async def tcustom(self, ctx, *, arg):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        toptext = arg

        max = 30

        if len(toptext) >= max:
            return await ctx.send(f"That's too long!! Make sure your character count is under {max}!!")

        check = await Bot.querycustom(self, ctx.author.id)

        if not check:
            await Bot.addtocustom(self, ctx.author.id)
            await Bot.updatecustom(self, ctx.author.id, "top", toptext)
            await ctx.send(f"Added custom top text to profile!")
        else:
            await Bot.updatecustom(self, ctx.author.id, "top", toptext)
            await ctx.send(f"Added custom top text to profile!")
            pass
        pass

    @tcustom.error
    async def ask_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Put what you want for your custom top text for your vprofile!")

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command()
    async def bcustom(self, ctx, *, arg):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        bottomtext = arg

        max = 20

        if len(bottomtext) >= max:
            return await ctx.send(f"That's too long!! Make sure your character count is under {max}!!")

        check = await Bot.querycustom(self, ctx.author.id)

        if not check:
            await Bot.addtocustom(self, ctx.author.id)
            await Bot.updatecustom(self, ctx.author.id, "bottom", bottomtext)
            await ctx.send(f"Added custom bottom text to profile!")
        else:
            await Bot.updatecustom(self, ctx.author.id, "bottom", bottomtext)
            await ctx.send(f"Added custom bottom text to profile!")
            pass
        pass

    @bcustom.error
    async def ask_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Put what you want for your custom bottom text for your vprofile!")

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(vibecheck2(bot))
