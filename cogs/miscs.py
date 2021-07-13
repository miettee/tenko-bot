import discord
from discord.ext import commands

from discord.ext.commands import AutoShardedBot
import asyncio
import os
import random
import sys


class miscs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.voice_dir = r"/root/tenko/resources/voice lines/tenko"
        # same deal as blessed cursed etc, all of these will be mp3 files of tenkos voice clips startig w tenko1.mp3 etc etc
        self.ffmpeg_location = "/usr/bin/ffmpeg"

    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("yo tenko,"):
            dangans = ['Makoto', 'Sayaka', 'Leon', 'Kyoko', 'Byakuya',
                       'Mondo', 'Toko', 'Celestia', 'Aoi', 'Kiyotaka',
                       'Sakura', 'Yasuhiro', 'Chihiro', 'Mukuro',
                       # end of 1 charas
                       'Hajime', 'Gundham', 'Kazuichi',
                       'Nekomaru', 'Fuyuhiko', 'Akane', 'Chiaki',
                       'Sonia', 'Hiyoko',
                       'Mahiru', 'Mikan',
                       'Ibuki', 'Peko',  # end of 2 charas
                       'Angie', 'Gonta',
                       'Himiko', 'Kaede', 'Kaito', 'Kiibo',
                       'Kirumi',
                       'Korekiyo', 'Maki', 'Miu', 'Rantaro', 'Ryoma', 'Shuichi', 'Tsumugi']

            answers = ['Possibly!', 'Hell yes!!',
                       'That\'s the best thing I\'ve ever heard in my life!! Even better than Neo-Aikido!! Are you some kind of genius?? Yes!!!!!!',
                       'Maybe?', 'Uhhh, no?', 'Nah.', 'No way!! What are you talking about?',
                       'Sure!', 'I am offended on behalf of all women!! How dare you!!?!!!!?!',
                       'That\'s hard to answer....',
                       'Why not!?', 'Of course!!!!', 'I mean, there\'s no reason not!', 'Hahahahah! No.',
                       'Sure thing!!!',
                       'I guess it\'s a possibility...?', 'NO!!!!', 'I can\'t believe you asked that...',
                       'That sort of question makes me think you don\'t respect women!',
                       'Yeah! I\'ve never been more certain in my life!!',
                       'I can\'t answer that now, I\'m too busy training!!', 'I\'ll ask Himiko about that one!',
                       'Nope!', 'No, that\'s wrong!', 'I\'m sure of it!',
                       'That\'s funny! I was thinking the same thing!!',
                       'Only a degenerate male would say that... I won\'t fall for it!!... If you are not, I apologise!!',
                       'One day!', 'Never!', 'I\'ll think about it.',
                       'Try again? I wasn\'t paying attention, I\'m sorry!',
                       'Well..', 'Oooh, that\'s a hard one! Hmm... ok!', 'Hmm.... no!', 'Okay! That sounds right!',
                       'I think so too!', 'Oh no, never! Whaaat??',
                       'I don\'t think I can answer that!! I\'m not qualified!', 'You know better than me!! I think??',
                       'Oh! Well, okay!!! ', 'Himiko said yes so I agree too!!',
                       'Himiko said no... I\'m gonna have to pass! Nope!',
                       f'Oooh, I think {random.choice(dangans)} knows about that!!', 'For sure!!',
                       'YES!!!! I TOTALLY SEE IT!!', '... I don\'t get it!! Haha!',
                       'Himiko was too tired to comment, but I think yes!!',
                       'To a degree, yes..?',
                       'That\'s a good question! Definitely no! Actually, it\'s a bad question now that I think about it.']

            self.log(message.content, message.author.name, message.guild.name, message.channel.name)
            himikolines = ['Did you say Himiko?? That\'s amazing!!',
                           'Himiko? Awh, don\'t you just love her??? I know I do!!',
                           'I saw Himiko just yesterday!! What a coincidence!! Are you like, spying on my life?',
                           'Oh, Himiko! I forgot, I needed to tell her something!! Thanks for reminding me!',
                           'Any question with Himiko in it is a great one!! Did you know she does REAL magic??',
                           "You know Himiko? Wow, I do too!!"]

            loves = ["I love you!!", "I can't love you..", "I don't know you!! Sorry!", "I only love neo-aikido!!",
                     "I'll try to love you!", "I love you as a friend!", "Not really!", "I don't love you at all!"]
            specials = ["himiko", "nagito", "kokichi", "love me", "seesaw", "kia"]
            specials2 = ["himiko", "nagito", "kokichi"]

            if any(e in message.content for e in specials):

                for s in ["love me"]:
                    if not any(e in message.content for e in specials2):
                        if s in message.content and "does" in message.content:
                            await message.channel.send("I'm sure they love you!")
                        elif s in message.content:
                            await message.channel.send(random.choice(loves))

                if "nagito" in message.content or "kokichi" in message.content:
                    await message.channel.send("That degenerate!!? I'm not talking about him..")

                if "himiko" in message.content:
                    await message.channel.send(random.choice(himikolines))

                if "seesaw" in message.content:
                    await message.channel.send("Hey!! That is not funny- no seesaws!!!")

                if "kia" in message.content:
                    await message.channel.send("Huh?? Kia cars are my favourite!! How did you know??!?")
                    # to kia people, here you go <3

            else:
                await message.channel.send(random.choice(answers))

        if message.content.startswith('tenko, who would'):
            self.log(message.content, message.author.name, message.guild.name, message.channel.name)
            try:
                msg_cont = message.content.lower()

                start = msg_cont.find("tenko, who would") + len("tenko, who would")
                end = msg_cont.find("?")

                verb = msg_cont[start:end]

                start = msg_cont.find("?") + len("?")
                end = msg_cont.find("or")

                first_word = msg_cont[start:end]

                start = msg_cont.find("or") + len("or")

                second_word = msg_cont[start:]
                second_word = f"{second_word} "

                await message.channel.send(
                    f'Oh! Well I know{random.choice([first_word, second_word])}would totally{verb}!')
            except:
                await message.channel.send(
                    'Hey, I don\'t know what you mean! Remember, you need to have two options and a question mark after your action, ok? Example: tenko, who would win? x or y')



    @commands.command()
    async def commandlist(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        eg = discord.Embed(

            description='All of my commands as of 19/3/21! My prefix is **t^** !!' \
                        '\n \n» **Fun Commands:**'.format(ctx.message) + \
                        '\n`hello` - Say hi to me!' \
                        '\n`spoiler` - Generates a random Danganronpa spoiler- is it real? I don\'t know!!' \
                        '\n`vibes` - Gives you a 100% accurate vibe check every 12 hours!' \
                        '\n`cursed` - Sends a random cursed Danganronpa image.' \
                        '\n`blessed` - Sends a random blessed Danganronpa image.' \
                        '\n`girl` - Sends a random Danganronpa girl! Idea credits to commentspaepanion#1422' \
                        '\n`speak` - Connects me and then disconnects me to a voice chat so I can speak my mind!!' \
                        '\n`degenerate` - I will rate how much of a degenerate anything is!!' \
                        '\n`ronpa` - Sends a random Danganronpa character, from any game!' \
                        '\n`ship` - I\'ll think up a ship just for you!!' \
                        '\n`drprofile` - I consult Shuichi on your role in a Danganronpa game!' \
 
                        '\n \n» **Fun (no prefix) commands:**'.format(ctx.message) + \
                        '\n`yo tenko,` - Asks me a yes or no question. I\'ll answer (almost) anything!' \
                        '\n`tenko, who would?` - I\'ll choose between two options seperated with an or! For example *tenko, who would win? x or y*' \
 
                        '\n \n» **Image manipulation commands!:**'.format(ctx.message) + \
                        '\n`portrait` - Puts your profile picture on the trial portrait!! ' \
                        '\n`counter` - Counter an argument with your profile picture!!' \
                        '\n`gameover` - Pretend your profile picture is being executed!!' \
                        '\n`cameo (scale)` - Cameo a random Danganronpa character into any image! Choose a number from 1 to 5 to set the scale - 1 is biggest, 5 is smallest! This defaults to your profile picture!' \
                        '\n \n» **Other Commands:**'.format(ctx.message) + \
                        '\n`help` - All my ultra important links are here!!' \
                        '\n`commands` - Wow!! That\'s this command!!'
                        '\n`rt` - Toggle off my reacts for the channel you\'re in!!',
            colour=0x008000

        )

        eg.set_author(name='Tenko Command List')
        eg.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/danganronpa/images/2/20/Danganronpa_V3_Tenko_Chabashira_Halfbody_Sprite_%2811%29.png/revision/latest/top-crop/width/300/height/300?cb=20180427071552')
        await ctx.message.channel.send(embed=eg)

    @commands.command(name='hello')
    async def hello(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        extra_messages = ['How\'s it going?', 'Women for the win!', 'HIIIYYYAAHH!!', 'Men suck!', 'Where\'s Himiko?',
                          'Let\'s go lesbians!', 'Wow, you look great today!!',
                          'Let\'s get moving!! 100 uppercuts, come on!!',
                          'How are you? I hope your day is full of Neo-Aikido!',
                          "Are you going to Himiko's magic show??", "All women are queens!!", "Oh, I love your outfit!",
                          "Let's get ice cream some day!!", "Isn't magic great??",
                          "Don't give up on your dreams!!! Or I'll punch you!!! Supportively!!",
                          "Don't worry, I'm here to protect you from all those degenerate males!!!",
                          "Did you know Neo-Aikido is the best martial art ever??? It's true!!",
                          "Wow!! Girls are great!!!"
            , "Respect women!!! Respect them more!!!", "Don't hold back!! It's alright to let out your emotions!!",
                          "Kaede is such a great pianist!! It really hypes me up for a workout!!",
                          "Kiibo's a robot.... does that still make him a degenerate male??",
                          "Himiko is so cool!!!! Don't you agree??"]
        await ctx.message.channel.send(
            f'Hey {{0.author.mention}}!! {random.choice(extra_messages)}'.format(ctx.message))

    @commands.command()
    async def help(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        eg = discord.Embed(
            description=
            '      ˏˋ°•*⁀➷'
            '\n\n[Tenko server](https://discord.gg/https://discord.gg/s9TFgCb) |  [Tenko invite](https://discordapp.com/oauth2/authorize?client_id=%20663427713654325278&scope=bot) | [Tenko vote](https://top.gg/bot/663427713654325278/vote)'
            # '\n \nTo join the support server, go to \n [here](https://discord.gg/https://discord.gg/s9TFgCb), for inviting Tenko to all your servers go to [here](https://discordapp.com/oauth2/authorize?client_id=%20663427713654325278&scope=bot), and to vote for her go to [here!](https://top.gg/bot/663427713654325278/vote) ' \
            '\n \nI\'m Tenko Chabashira, keeping the degenerate males away one punch at a time! To see a detailed list of commands, use t^commands! '.format(
                ctx.message),
            colour=0x008000
        )
        eg.set_footer(text="Created by: aubee#4504 ")  # thatsa me, keep it in there
        eg.set_author(name='Tenko Help',
                      icon_url="https://vignette.wikia.nocookie.net/danganronpa/images/7/7b/Danganronpa_V3_Tenko_Chabashira_Fullbody_Sprite_%281%29.png/revision/latest/top-crop/width/220/height/220?cb=20180427070540")
        eg.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/danganronpa/images/f/f7/Danganronpa_V3_Tenko_Chabashira_Halfbody_Sprite_%2827%29.png/revision/latest/top-crop/width/300/height/300?cb=20180427071730')
        await ctx.message.channel.send(embed=eg)

    @commands.command()
    async def spoiler(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        chap = ['chapter 1!', 'chapter 2!', 'chapter 3!', 'chapter 4!', 'chapter 5!']
        shock = [' How shocking!!', ' Huh!?!', ' Wow!', ' Probably!!', ' Wild!!', " Wait, really??", " What!!?",
                 " Haha, wow!!", " That's amazing!!", " Woah!!"]
        dangan1 = ['Makoto Naegi', 'Sayaka Maizono', 'Leon Kuwata', 'Kyoko Kirigiri', 'Byakuya Togami', 'Hifumi Yamada',
                   'Mondo Owada', 'Toko Fukawa', 'Celestia Ludenberg', 'Aoi Asahina', 'Kiyotaka Ishimaru',
                   'Sakura Ogami',
                   'Yasuhiro Hagakure', 'Junko Enoshima', 'Chihiro Fujisaki',
                   'Mukuro Ikusaba', 'Monokuma']
        dangan2 = [
            'Hajime Hinata', 'Nagito Komaeda',
            'Gundham Tanaka', 'Kazuichi Soda',
            'Teruteru Hanamura', 'Nekomaru Nidai',
            'Fuyuhiko Kuzuryu', 'Akane Owari',
            'Chiaki Nanami',
            'Sonia Nevermind', 'Hiyoko Saionji',
            'Mahiru Koizumi', 'Mikan Tsumiki',
            'Ibuki Mioda', 'Peko Pekoyama',
            'Monomi', 'Impostor']
        dangan3 = [
            'Angie Yonaga',
            'Gonta Gokuhara',
            'Himiko Yumeno',
            'Kaede Akamatsu', 'Kaito Momota', 'Kiibo',
            'Kirumi Tojo', 'Kokichi Oma',
            'Korekiyo Shinguuji', 'Maki Harukawa', 'Miu Iruma', 'Rantaro Amami', 'Ryoma Hoshi', 'Shuichi Saihara',
            'Tenko Chabashira', 'Tsumugi Shirogane']

        mylists = [("In Danganronpa: Trigger Happy Havoc, ", dangan1),
                   ("In Danganronpa 2: Goodbye Despair, ", dangan2),
                   ("In Danganronpa v3: Killing Harmony, ", dangan3)]

        (textforthisgame, listforthisgame) = random.choice(mylists)

        def get_rightlist(chara, chara2):
            if chara2:
                listforthisgame_c = listforthisgame
                listforthisgame_c.remove(chara2)

            else:
                listforthisgame_c = listforthisgame
                listforthisgame_c.remove(chara)

            return random.choice(listforthisgame_c)

        p_o_f = random.choice(listforthisgame)

        chapterr = random.choice(chap)

        secondc = get_rightlist(p_o_f, False)
        thirdc = get_rightlist(p_o_f, secondc)

        possibles = [f' was killed by {secondc} in {chapterr}',
                     f' killed {secondc} in {chapterr}',
                     ' is the mastermind!!', ' is the traitor!!']

        if chapterr == 'chapter 3!':
            possibles = [f' was killed by {secondc} in {chapterr}',
                         f' killed {secondc} and {thirdc} in {chapterr}',
                         ' is the mastermind!!', ' is the traitor!!']

        ms = discord.Embed(
            description=f"{textforthisgame}{p_o_f}{random.choice(possibles)}{random.choice(shock)}",
            colour=0x008000
        )
        ms.set_author(name=f"Watch out!! Spoilers!")
        await ctx.message.channel.send(embed=ms)

    @commands.command()
    async def servers(self,ctx):
        msg = f"I'm in {len(self.bot.guilds)} servers!"
        await ctx.send(msg)

    @commands.command()
    async def speak(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.message.channel.send("Hey! You have to join a voice channel to hear me!")
            return

        voice = ctx.author.voice.channel

        if ctx.voice_client:
            await ctx.send("Slow down!! Let me finish!")
            return
        else:
            vc = await voice.connect()

        my_files = []
        for i in range(1, 21):
            my_files.append(rf"{self.voice_dir}{str(i)}.mp3")

        vc.play(discord.FFmpegPCMAudio(source=(random.choice(my_files)),
                                       executable=self.ffmpeg_location),
                )
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 10.0
        while vc.is_playing():
            await asyncio.sleep(0.5)
        vc.stop()
        await vc.disconnect()

    # degenerate - start

    @commands.command()
    async def degenerate(self,ctx):

        dg_no = []
        for i in range(0, 101):
            dg_no.append(i)

        for e in dg_no:
            str(e)

        dg_phrases = ["Not an atom of degenerate to be seen!! I LOVE that!!! That's my kind of rating!!",
                      "Only a tiny tiny tiny speck!! Amazing! My kind of rating!!",
                      "Only a dust spec! Basically good!!", "A tiny litte bit, but that hardly matters!!",
                      "It's barely a problem, honestly! That's fine!", "Wowie, it's barely there!",
                      "A tiny smidge! Maybe a wash would be good?", "Only a sliver of degeneracy!!",
                      "A smaalll bit! I'm ok with that!", "Pretty ok!", "Not too bad! There's not much there at all!",
                      "Actually not so bad!", "Well, not so bad!", 'Hmm, not so bad! But isn\'t that unlucky?',
                      "I think that's not bad!", "Hmmm hmm hmm, not bad at all!", "Not super bad!",
                      "Well, it's not super bad!", "I think that's just ok! Not super bad.", "Pretty alright!",
                      "Could be improved a bit??",
                      "Room for improvement? Just a little??", "Ok, but could be a little better!!",
                      "Mostly fine, could be improved a small bit.", "I'll let it slide!",
                      "I think I can let it slide??", "I can probably let it slide!", "Well, I can let it slide!",
                      "Mostly fine, I'll try to let it slide!", "I'm sure that it can be improved, so I'll let it off.",
                      "Maybe it's time to improve that...? Punching things always helps for me!",
                      "A little bit of a degenerate, but it's not a huge problem",
                      "Decently degenerate, but not a massive issue!",
                      "A fair little bit of degeneracy, but what else could be expected?",
                      "Well there's certainly some there, but it's not a huge problem?",
                      "Hmm, a fair bit of degeneracy there.", "Hmm hmm, there's a bit there..",
                      "Weelll,, there is some degeneracy there!! Sorry!", "Aw, there's some degeneracy there!",
                      "Sadly, there is some degeneracy there", "Unfortunate!! But not the worst..?",
                      "Not the worst, but not the best?", "I think that could be a lot better!", "How average!",
                      "Wow, that's average!", "Not awful, just average!", "Hmm, a mostly average score",
                      "This could be better! Being average is boring!", "Averagely strong degeneracy.",
                      "Huh, it's almost half and half!",
                      "Oh, wow! Equal degeneracy and non-degeneracy! That's pretty cool?",
                      "Oh no!! It's on the verge of degeneracy!!", "Well, it's just about more degenerate than not!",
                      "This could be so much better!!!", "Aw, it's tipped the scales!!", "It's becoming a problem..",
                      "There's probably a problem there!!", "Noo! That's a bit of a problem!",
                      "It's not too late to become better!", "A problem, but it's not too late yet!",
                      "There better be improvement quickly, or it'll keep getting worse!",
                      "A secret degenerate, huh??", "I doubt passing as a non degenerate would even be an option.",
                      "Don't think I can't tell that there's degenerate energy there!", "Certain degenerate energy..",
                      "Lots of degenerate energy!", "Reaching dangerous levels there...",
                      "Oh no! It's reaching dangerous degenerate levels!", "A severe amount of degenerate vibes..",
                      "Haha! That's an... amusing level of degeneracy. But it doesn't excuse it!!",
                      "There's no going back from that level!",
                      "Aha! That's some degeneracy!", "I'd be able to spot that level of degeneracy anywhere!",
                      "A definite degenerate! How unfortunate!", "Yep, definitely a degenerate.",
                      "Certainly a degenerate! That's really bad!", "A typical degenerate..", "What a degenerate...",
                      "What a degenerate!", "A no good degenerate!",
                      "I could sense that degeneracy from a mile away! Ten miles!!",
                      "Disgustingly degenerate! Go away!", "Imagine being such a degenerate! Ew!",
                      "That's the sort of degeneracy I'd punch!", "That sort of degeneracy, I'd throw across a room!",
                      "It's making me want to go punch things!!", "Is it enjoyable, being THAT much of a degenerate!!?",
                      "Degenerate alert! I hate that so much!!",
                      "Wow, that's really, really bad!! I'm gonna go punch things now!",
                      "Get out of my sight degenerate!! That's disgusting!!!!",
                      "I didn't know it was possible to be THIS bad? Degenerates never fail to amaze me!!!",
                      "How is this possible?? Really, I'd be amazed!! If I wasn't so repulsed!!",
                      "Truly, truly, the worst levels of degeneracy...",
                      "Get away from me this INSTANT, degenerate! I can barely say that name! Without throwing things!",
                      "Revolting!! That sort of degeneracy should not go unpunished!!",
                      "You know, I'd expect that level of degeneracy from Byakuya...",
                      "Ughh, that's the sort of degeneracy I'd expect from Nagito...",
                      "This is awful!! That's Kokichi level degeneracy!!",
                      "This is every male ever combined levels of degeneracy!!",
                      "These are despairing levels of degeneracy.....",
                      "Congratulations!!! That's the worst level of degeneracy I've ever seen, ever! That's not an achievement!!"]

        dg_dict = {}
        for i in range(0, 101):
            dg_dict.update({
                dg_no[i]: dg_phrases[i]})

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        try:
            sent_percent = random.choice(dg_no)
            sent_msg = dg_dict.get(sent_percent)
            item = ctx.message.content
            item = item[13:]
            if item == "":
                await ctx.message.channel.send(
                    f"Oh, that's an error! Make sure that you've actually put in something for me to rate!")
            else:
                await ctx.message.channel.send(f"I degene-rate **{item}** a {sent_percent}%! {sent_msg}")
        except AttributeError as error:
            await ctx.message.channel.send(
                f"Hey, make sure that you've actually put in something for me to rate!")
            print(error)



def setup(bot):
    bot.add_cog(miscs(bot))
