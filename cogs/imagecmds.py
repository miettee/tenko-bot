import discord
from discord.ext import commands
import random



class imagecmds(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot

        self.blessed_dir = "/root/tenko/resources/blessed/blessed"
        self.girl_dir = "/root/tenko/resources/girl/girl"
        self.cursed_dir = "/root/tenko/resources/cursed/cursed"
        self.ronpa_dir = "/root/tenko/resources/dangans/dangan"

        #make sure ur image files all start with the word at the end, and ascend in number for each file dir, eg blessed1.png, blessed2.png, blessed1.jpg etc

    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")

    @commands.command()
    async def cursed(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        my_files = []
        for i in range(1, 162): #nb range limits cant go beyond how many files you compile
            my_files.append(
                discord.File(f"{self.cursed_dir}{i}.jpg"))
        for i in range(1, 96):
            my_files.append(
                discord.File(f"{self.cursed_dir}{i}.png"))
        for i in range(1, 6):
            my_files.append(
                discord.File(f"{self.cursed_dir}{i}.jpeg"))

        await ctx.channel.send(files=[(random.choice(my_files))])

    @commands.command()
    async def girl(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        my_files = []
        for i in range(1, 88):
            my_files.append(
                discord.File(f"{self.girl_dir}{i}.png"))

        await ctx.message.channel.send(files=[(random.choice(my_files))])

    @commands.command()
    async def blessed(self, ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        my_files = []
        for i in range(1, 58):
            my_files.append(
                discord.File(f"{self.blessed_dir}{i}.jpg"))
        for i in range(1, 202):
            my_files.append(
                discord.File(f"{self.blessed_dir}{i}.png"))
        for i in range(1, 7):
            my_files.append(
                discord.File(f"{self.blessed_dir}{i}.jpeg"))

        await ctx.message.channel.send(files=[(random.choice(my_files))])


    @commands.command()
    async def ronpa(self, ctx):
        messages_list = ['extra']  # extra unused item in the list because my file numbers start with 1 not 0
        danganss = ['Makoto Naegi', 'Sayaka Maizono', 'Leon Kuwata', 'Kyoko Kirigiri', 'Byakuya Togami',
                    'Hifumi Yamada',
                    'Mondo Owada', 'Toko Fukawa', 'Celestia Ludenberg', 'Aoi Asahina', 'Kiyotaka Ishimaru',
                    'Sakura Ogami', 'Yasuhiro Hagakure', 'Chihiro Fujisaki', 'Mukuro Ikusaba', 'Junko Enoshima',

                    'Hajime Hinata', 'Nagito Komaeda', 'Gundham Tanaka', 'Kazuichi Soda',
                    'Teruteru Hanamura', 'Nekomaru Nidai', 'Fuyuhiko Kuzuryu', 'Akane Owari', 'Chiaki Nanami',
                    'Sonia Nevermind', 'Hiyoko Saionji',
                    'Mahiru Koizumi', 'Mikan Tsumiki',
                    'Ibuki Mioda', 'Peko Pekoyama',
                    'Angie Yonaga', 'Gonta Gokuhara',
                    'Himiko Yumeno', 'Kaede Akamatsu', 'Kaito Momota', 'Kiibo',
                    'Kirumi Tojo', 'Kokichi Oma',
                    'Korekiyo Shinguuji', 'Maki Harukawa', 'Miu Iruma', 'Rantaro Amami', 'Ryoma Hoshi',
                    'Shuichi Saihara',
                    'Tenko Chabashira',
                    'Tsumugi Shirogane',
                    'Izuru Kamazura']  # your images will need to be in the same order as the characters
        talents = ['Lucky Student', 'Pop Sensation', 'Baseball Player', 'Detective', 'Heir', 'Doujin Artist'
            , 'Gang Leader', 'Author', 'Gambler', 'Swimmer', 'Moral Compass', 'Martial Artist',
                   'Fortune Teller', 'Programmer', 'Soldier', 'Despair/Fashionista', 'Reserve Student', 'Lucky Student',
                   'Animal Breeder', 'Mechanic', 'Cook', 'Team Manager', 'Yakuza', 'Gymnast', 'Gamer', 'Princess'
            , 'Traditional Dancer', 'Photographer', 'Nurse', 'Musician', 'Swordswoman', 'Artist',
                   'Entomologist', 'Mage', 'Pianist', 'Astronaut', 'Robot', 'Maid', 'Supreme Leader', 'Anthropologist',
                   'Child Caregiver',
                   'Inventor', '???', 'Tennis Player', 'Detective', 'Aikido Master', 'Cosplayer']  # same for talents
        for i in range(0, 47):
            messages_list.append(
                f'Your assigned Danganronpa character is {danganss[i]}, the Super Highschool Level {talents[i]}!')
        specials_ = ["Your assigned Danganronpa character is Monokuma, Hope\'s Peak\'s headmaster!",
                     "Your assigned Danganronpa character is Izuru Kamakura, the Super Highschool Level Hope!",
                     "Your assigned Danganronpa character is the Super Highschool Level Impostor!",
                     "Your assigned Danganronpa character is Usami, the Magical Girl teacher!"]
        for e in specials_:
            messages_list.append(e)
        image_and_message = {}
        for i in range(1, 51):
            image_and_message.update({
                discord.File(fr"{self.ronpa_dir}{str(i)}.png"):
                    messages_list[i]})  # adds image files and messages as pairs in a dict

        sent_image = random.choice(list(image_and_message))  # gets a random image
        sent_text = image_and_message.get(sent_image)  # gets the messages from that image

        await ctx.message.channel.send(sent_text, files=[sent_image])  # sends message and image



def setup(bot):
    bot.add_cog(imagecmds(bot))
