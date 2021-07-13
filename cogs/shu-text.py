
from discord.ext import commands
import random
import json
import os
import discord
class txts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.talents_json = r"/root/tenko/resources/shuichi stuff/talents.json"
        #where EVERY talent is

    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")


    @commands.command()
    async def ship(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        danganss = ['Makoto Naegi', 'Sayaka Maizono', 'Leon Kuwata', 'Kyoko Kirigiri', 'Byakuya Togami',
                    'Hifumi Yamada',
                    'Mondo Owada', 'Toko Fukawa', 'Celestia Ludenberg', 'Aoi Asahina', 'Kiyotaka Ishimaru',
                    'Sakura Ogami', 'Yasuhiro Hagakure', 'Chihiro Fujisaki', 'Mukuro Ikusaba',
                    # end of 1 charas
                    'Hajime Hinata', 'Nagito Komaeda', 'Gundham Tanaka', 'Kazuichi Soda',
                    'Teruteru Hanamura', 'Nekomaru Nidai', 'Fuyuhiko Kuzuryu', 'Akane Owari', 'Chiaki Nanami',
                    'Sonia Nevermind', 'Hiyoko Saionji',
                    'Mahiru Koizumi', 'Mikan Tsumiki',
                    'Ibuki Mioda', 'Peko Pekoyama',  # end of 2 charas
                    'Angie Yonaga', 'Gonta Gokuhara',
                    'Himiko Yumeno', 'Kaede Akamatsu', 'Kaito Momota', 'Kiibo',
                    'Kirumi Tojo', 'Kokichi Oma',
                    'Korekiyo Shinguuji', 'Maki Harukawa', 'Miu Iruma', 'Rantaro Amami', 'Ryoma Hoshi',
                    'Shuichi Saihara',
                    'Tenko Chabashira', 'Tsumugi Shirogane']

        danganchoice1 = random.choice(danganss)
        danganchoice2 = random.choice(danganss)
        if danganchoice1 == danganchoice2:
            danganchoice1 = random.choice(danganss)

        drsplit1 = danganchoice1.split(' ')[random.randint(0, (len(danganchoice1.split(' ')) - 1))]
        if danganchoice1 == 'Nekomaru Nidai':
            drsplit1 = danganchoice1.split(' ')[0]

        drsplit2 = danganchoice2.split(' ')[random.randint(0, (len(danganchoice2.split(' ')) - 1))]

        go_one = drsplit1[0: random.randint(2, len(drsplit1) - 1)]
        go_two = drsplit2[0: random.randint(2, len(drsplit2) - 1)]
        if len(go_one) == len(drsplit1) - 1 or len(go_one) == len(drsplit1) - 2:
            try:
                go_two = drsplit2[0: random.randint(2, len(drsplit2) - 3)]
            except ValueError:
                go_two = drsplit2[0: random.randint(2, len(drsplit2) - 1)]

        combined_name = f"The ship name.. it's got to be {go_one}{go_two.lower()}!"

        checker = []
        comments = [" would make the best couple ever!!", " would make an.. okay couple?? I guess?",
                    " would make a really weird couple!!", " would make a very powerful couple!!!",
                    " would make a super happy couple!!", " would make an..... interesting?? couple??",
                    " would make a pretty bland couple, honestly!",
                    " would make a very annoying couple!", " would not work at all together as a couple!!",
                    "... could possibly work as a couple??", " would be a fan favourite couple! Totally!",
                    " would be a problematic couple!!", " would be a very cute couple together! Aww!!",
                    " would be a kind of abrasive as a couple...",
                    " would make a fine couple!",
                    " would be a great platonic ship!", " would be best as a platonic ship, definitely!",
                    " would most likely be happiest in a platonic ship.", " would be one of the best ships out there!!!",
                    " would be one of the strangest ships out there..??",
                    " would be a very supportive couple!", " would be a challenging couple to support, I think??",
                    " would, in my opinion, not work very well together? But they could work on it!!",
                    " would help each other grow and heal as a couple!",
                    " would be a weird couple, but they would be happy together, so that's what matters!!",
                    " would make THE PERFECT COUPLE!!",
                    " would be a couple in private.", " would be a very public couple!!",
                    " would be a little toxic as a couple..??"]
        comment = random.choice(comments)
        checker.append(danganchoice1)
        checker.append(danganchoice2)

        problematic = [["Toko Fukawa", "Byakuya Togami"], ["Kazuichi Soda", "Sonia Nevermind"],
                       ['Teruteru Hanamura', "Sonia Nevermind"], ["Hifumi Yamada", "Celestia Ludenberg"],
                       ["Hifumi Yamada", "Chihiro Fujisaki"], ["Hiyoko Saionji", "Mikan Tsumiki"],
                       ["Korekiyo Shinguuji", "Tenko Chabashira"]]
        for i in range(0, len(problematic)):
            if set(checker) == set(problematic[i]):
                comment = "... hey, wait a second? Who would even ship this????"
                combined_name = ""
        special_ships = {
            ("Shuichi Saihara", "Kaede Akamatsu"): ".. oh, those two?? I'd be super happy for them!!!!",
            ("Kaito Momota", "Maki Harukawa"): "... aww, don't they look cute together??",
            ("Himiko Yumeno", "Tenko Chabashira"): ".......... !!!!!!! !!!! !!",
            ("Mahiru Koizumi", "Hiyoko Saionji"): "... aww, they're so perfect for each other!! Platonic or romantic!!",
            ("Mondo Owada", "Kiyotaka Ishimaru"): ".. I think they work great together!! ",
            ("Nagito Komaeda", "Hajime Hinata"): "... this one's popular!!! Wow!!",
            ("Tenko Chabashira", "Kaede Akamatsu"): "... oh, Kaede?? She's amazing!! Would she even.....???"}


        for k in special_ships:
            if set(checker) == set(k):
                comment = special_ships.get(k)
        name = ctx.message.author.name

        emby = discord.Embed(
            description=f"*{danganchoice1}* and *{danganchoice2}*{comment} {combined_name}",
            colour=0x008000

        )
        emby.set_author(name=f"A ship for {name}!")
        await ctx.send(embed=emby)


    @commands.command()
    async def drprofile(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        with open(self.talents_json) as f:
            talent = json.load(f)

        chap_number = random.randint(1, 6)
        gotaway = False

        surviv_msg = ""

        fan_opinion = ["The fandom would adore you!", "Most fans would forget about you sadly...",
                       "You'd be infamous in the fandom.", "You'd be cherished by the fandom.",
                       "You'd be hated by the fandom!", "Most fans wouldn't care for you.",
                       "You'd be a hotly debated character!", "The fandom would be ok with you!",
                       "The fandom would obsess over you quite a bit...", "You'd be a number one comfort character.",
                       "Lots of people would kin you in the fandom", "You'd be accepted by the fandom ok.",
                       "You would be both loved and hated by the fandom!",
                       "The fandom would love to write fanfiction about you.",
                       "The fandom would be on the fence about you.", "The fandom would draw you lots!",
                       "You'd be shipped a lot with lots of characters!", "The fandom would love and appreciate you.",
                       "You'd be a character that people write essays about!",
                       "You'd be universally hated by fans and passers by.",
                       "You'd be loved intensely by a small portion of the fanbase.",
                       "You'd be a little popular in some parts of the fandom.",
                       "Every fan has probably had enough of seeing you!",
                       "You'd have a dedicated cult following in the fandom. Sounds like someone I know...",
                       "The fandom would think you had missed potential...",
                       "The fandom would think you deserved better!", "The fandom would redesign your outfit a lot.",
                       "The fandom would dislike you, mostly."]
        gotaway_chance = random.randint(1, 30)
        mastermind_chance = random.randint(1, 20)
        antag_chance = random.randint(1, 15)

        if gotaway_chance == 30:
            gotaway = True
        if mastermind_chance == 20:
            possibility = "m"
            chap_number = 6
        elif antag_chance == 15:
            possibility = "a"
            chap_number = random.randint(4, 6)
        elif chap_number == 6:
            possibility = "s"
        else:
            possibility = "mb"

        if chap_number == 6:
            surviv_msg = "Yes, you've got that survivor feeling to you."
            if possibility == "m":
                surviv_msg = "Hm, I would have thought you'd have survived, but it seems at the very last moment you were found out..."

        elif chap_number < 3:
            if gotaway:
                surviv_msg = "Huh, the game ended very early for you."
            else:
                surviv_msg = "That's a shame, dying early. I'm very sorry!"

        elif chap_number >= 3 and chap_number != 6:

            if gotaway:
                surviv_msg = "Huh, the game ended a bit later for you."
            else:
                surviv_msg = "Surviving for a fair amount of chapters, that's really impressive!"


        # four outcomes, a survivor, murdered or a blalckened, an antag or a mastermind

        def if_morb():

            b_txt = ["Oh, you'd murder someone... but you'd get found out! After a long trial, that is.",
                     "Oh, you'd murder someone... but not very well. You'd get caught almost immediately!",
                     "Oh, you'd murder someone... but in self defense. That's really unfortunate.",
                     "You'd be the victim there, sadly.",
                     "You'd make the first move to kill, but you'd end up the victim.",
                     "You'd be the victim, but your murder would never be fully solved... I'm sorry about that.",
                     "You'd be the victim, but at least your killer would be brought to justice pretty fast."]
            outcome = random.choice(b_txt)
            d_descs = ["Your death would be really sad, and you'd be missed.", "Your death would be quite average.",
                       "Your death would be very shocking!",
                       "Your death would be overshadowed by the events that occur next.",
                       "Your death would be emotionally devastating. I'm crying a little thinking about it...",
                       "Your death would be undeserved.", "Your death would be... a little deserved.",
                       "Your death would be very deserved. Hm."]
            death_desc = random.choice(d_descs)

            if gotaway:
                outcome = "Oh, you'd murder someone... and get away with it? I don't think I've ever heard of someone doing that before.."
                death_desc = "So you'd be just fine, but all your classmates would die."

            final_descs = ["I think you'd be fun to be around!", "I think you'd be very serious.",
                           "I think you'd have a cut off character arc.", "I think you'd lose someone that you'd love.",
                           "I think you'd constantly make things harder for everyone.",
                           "I think you'd be a litte forgettable.",
                           "I think you'd be babey... is that the the correct term?",
                           "I think you'd be wild and obsessive.", "I think you'd be gloomy and nihilistic.",
                           "I think you'd be a realist.", "I think you'd make the best of things.",
                           "I think you'd somehow enjoy the killing game?"]

            return f"I can tell by looking at you that you'd be the Ultimate {random.choice(talent)}. Mmm, you'd make it to Chapter... {chap_number}? {surviv_msg}\n\n{outcome} {death_desc}\n\n{random.choice(final_descs)} {random.choice(fan_opinion)}"

        def if_survive():
            protag = False
            notmorb_descs = [
                "You'd have some close calls, though. You'd be suspected quite a lot throughout each trial, because you'd tend to be in the wrong place a lot.",
                "You'd sail through without doing much at all. That's alright, surviving is still a great achievment!",
                "I guess surviving is a given though, since you'd definitely be the protagonist! You'd be at the forefront of every investigation.",
                "You'd be mostly in the background, so no one would pay much attention to you. That's a perfectly reasonable tactic!",
                "You'd get plot armour midway through, from a dramatic event or some interesting character development."]
            notmorb_desc = random.choice(notmorb_descs)
            if notmorb_desc == "I guess surviving is a given though, since you'd definitely be the protagonist! You'd be at the forefront of every investigation.":
                protag = True
            final_descs = ["Throughout the game you'd keep very positive!",
                           "Throughout the game you'd be quiet and subdued.",
                           "Throughout the game you'd slowly change for the better!",
                           "Throughout the game you'd get a love interest! They would survive with you.",
                           "Throughout the game you'd be very annoying, a little like Kokichi..."]

            if protag:
                protag_descs = [
                    "Overall you'd be a solid and reliable protagonist. Everyone would respect the actions you'd take and the way you'd handle things.",
                    "Mostly you'd be a decent protagonist, although you would do the bare minimum, to be honest.",
                    "I think you'd be a fantastic protagonist, and you'd be loved by almost everyone!"]
                final = random.choice(protag_descs)
            else:
                final = random.choice(final_descs)

            return f"I can tell by looking at you that you'd be the Ultimate {random.choice(talent)}. Mmm, you'd make it to Chapter... {chap_number}? {surviv_msg}\n\n{notmorb_desc}\n\n{final} {random.choice(fan_opinion)} Along with all the other survivors, you'd escape Danganronpa, just about!"

        def if_mastermind():
            mastermind_desc = ["Oh, you'd be the mastermind of your killing game?... That's awful.",
                               "You'd definitely be the mastermind of the killing game.",
                               "You'd be the mastermind of the killing game, wouldn't you?"]
            mastermind_rate = [
                "Well, it looks like you'd be a pretty good mastermind, all things considered. No one would suspect a thing until the very last moment...",
                "Well, it looks like you'd be pretty bad at it. ",
                "Well, it looks like you'd be a very interesting mastermind, I think.",
                "Well, it looks like you'd at least be a sympathetic mastermind. I think you'd be sad for your friends.",
                "It looks like you'd pretend it was all Junko Enoshima... sounds like someone I know.",
                "Well, it looks like you'd be a very competent mastermind, in my opinion."]
            final_descs = ["Throughout the game you'd keep very quiet, so as not to attract attention.",
                           "Throughout the game you'd be loud and outgoing.",
                           "Throughout the game you'd pretend to hate the killing game with all your heart... ",
                           "Throughout the game you'd keep to the sidelines.",
                           "Throughout the game you'd try to ignite conflict from everyone..."]

            return f"I can tell by looking at you that you'd be the Ultimate {random.choice(talent)}. Mmm, you'd make it to Chapter... {chap_number}? {surviv_msg}\n\n{random.choice(mastermind_desc)} {random.choice(mastermind_rate)}\n\n{random.choice(final_descs)} {random.choice(fan_opinion)}"

        def if_antag():

            antag_desc = ["Ah, you'd be the antagonist. Well, I guess every killing game needs one...",
                          "Ah, you'd be the one making everything harder for everyone. I know someone just like you...",
                          "Looks like you'd be the antagonist, unfortunately."]
            antag_rate = ["As all antags go, you wouldn't be the worse.",
                          "You'd love messing with trials, for some reason.",
                          "You'd be a respectable antag, you would still have some morals.",
                          "You would be an obsessive antag.",
                          "You wouldn't think you were the antag, but you definitely would be.",
                          "You'd be a behind the scenes antag.",
                          "You'd be very annoying as an antag, but you wouldn't do much harm.",
                          "You'd be pretty bad as an antag, but you'd also help out in trials.",
                          "You'd be the worst antag I've ever heard of!", "You'd be a conflicted antag."]

            final_descs = ["Throughout the game everyone would hate you.",
                           "Throughout the game you'd be heavily ignored.",
                           "Throughout the game you'd keep up a charade.",
                           "Throughout the game several people would attempt to kill you on multiple occasions.",
                           "Throughout the game you'd be grudgingly respected."]
            if chap_number == 6:
                die_msg = ["Although you'd have survived, no one would be pleased about it.",
                           "I think you'd probably get redeemed near the end of the killing game.",
                           "It's very suprising that you survived actually. But I'm sure you'd start to become a better person because of it! Maybe."]
            else:
                die_msg = ["Your death would be the most shocking of them all.",
                           "Your death would be horrifying, but it would help uncover a secret.",
                           "Your death would be incredibly difficult to solve, and would only be figured out at the very last moment.",
                           "Your death would impact everyone around you in many different ways.",
                           "Your death would be... suprisingly anticlimatic.",
                           "Your death would be quite average, suprisingly. Maybe there would be something more to it..."]

            return f"I can tell by looking at you that you'd be the Ultimate {random.choice(talent)}. Mmm, you'd make it to Chapter... {chap_number}? {surviv_msg}\n\n{random.choice(antag_desc)} {random.choice(antag_rate)}\n\n{random.choice(die_msg)}\n\n{random.choice(final_descs)} {random.choice(fan_opinion)}"

        def get_path(x):
            return {
                'a': if_antag,
                'mb': if_morb,
                'm': if_mastermind,
                's': if_survive
            }.get(x)

        msg = get_path(possibility)()

        user = ctx.message.author.name

        profilee = ctx.message.content[12:]

        if profilee == "":
            intro_msg = f"What Shuichi thinks you'd be like in Danganronpa, {user}!"
        else:
            if len(profilee) > 255:
                await ctx.message.channel.send("Haha!! That's... too long.")
                return
            intro_msg = f"What Shuichi thinks {profilee} would be like in Danganronpa!"
            for r in (("you would", "they would"), ("you survived", "they survived"), ("you deserved", "they deserved"),
                      ("You'd", " They'd"), ("your", "their"), ("you,", "them,"), ("you ", "them "),
                      ("you had", "they had"),
                      ("Your", "Their"), ("You", "Them"), ("you.", "them."), ("you wouldn't", "they wouldn't"),
                      ("you were", "they were"), ("you definitely", "they definitely"),
                      ("yours", "theirs"), ("you're", "they're"), ("they've,", "you've"), ("you'd", "they'd"),
                      ("you had", "they had"),
                      ("you deserved", "they deserved"), ("you lots", "they lots"), ("you!", "them!"),
                      ("you?", "they?")):
                msg = msg.replace(*r)

        # ^ TERRIBLE way of doing it lmaoo

        ms = discord.Embed(
            description=msg,
            colour=0x008000

        )

        ms.set_author(name=f"{intro_msg}")
        await ctx.message.channel.send(embed=ms)


        #lot of text in this one lol


def setup(bot):
    bot.add_cog(txts(bot))
