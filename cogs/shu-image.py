
from PIL import Image, ImageSequence, ImageDraw
from discord.ext import commands
from io import BytesIO
import random
import discord
import sys
import traceback
import os


class ded(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



        self.thatswrong = r"/root/tenko/resources/shuichi stuff/nothatswrong.jpg"
        self.stand = r"/root/tenko/resources/shuichi stuff/portrait.png"
        self.cross = r"/root/tenko/resources/shuichi stuff/crosss.png"
        self.canvas = r"/root/tenko/resources/shuichi stuff/canvas.png"
        self.cameoo = r"/root/tenko/resources/full body sprites"
        self.file_gameover_gif = r"/root/tenko/resources/shuichi stuff/game over 2.gif"

    def log(self, logmsg, user, server, channel):
        print(f"{logmsg}  by `{user}` in `{server}`, in channel `{channel}`")



    @commands.command(name='cameo')
    async def cameo(self,ctx, arg):

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        try:
            ratio_ = int(arg)
        except ValueError:
            return await ctx.send("Specify a whole number between 1 and 5 for the size of your cameo!")

        if ratio_ > 5 or ratio_ <1:
            return await ctx.send("The cameo size has to be between 1 and 5!!")

        if ctx.message.attachments:
            asset = await ctx.message.attachments[0].read()
            imported = Image.open(BytesIO(asset))

        elif ctx.message.mentions:
            asset = await ctx.message.mentions[0].avatar_url.read()
            imported = Image.open(BytesIO(asset))
        else:
            Asset = ctx.message.author.avatar_url
            imported = Image.open(BytesIO(await Asset.read()))

        width, height = imported.size

        ratio_w = round(width / ratio_)
        ratio_h = round(height / ratio_)

        randw = random.randint(0, width - round(ratio_w / 2))
        randh = random.randint(0, height - round(ratio_h / 2))

        thethin = random.choice(os.listdir(f'{self.cameoo}'))

        thesprite = Image.open(fr'{self.cameoo}/{thethin}')

        size = ratio_w, ratio_h
        thesprite.thumbnail(size)
        thesprite = thesprite.convert("RGBA")

        imported.paste(thesprite, (randw, randh), mask=thesprite)
        io_object = BytesIO()
        imported.save(io_object, 'PNG', save_all=True)
        io_object.seek(0)
        try:
            await ctx.channel.send(file=discord.File(io_object, 'dr_cameo.png'))
        except discord.errors.HTTPException:
            return await ctx.send("Your image was too big!!")

    @cameo.error
    async def cameo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f'How big will the cameo be? You have to choose a number between 1, the biggest, and 5, the smallest!')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


    @commands.command(name='portrait', aliases=["ded", "dead"])
    async def portrait(self, ctx):

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        if ctx.message.attachments:
            asset = await ctx.message.attachments[0].read()
            imported = Image.open(BytesIO(asset))

        elif ctx.message.mentions:
            asset = await ctx.message.mentions[0].avatar_url.read()
            imported = Image.open(BytesIO(asset))
        else:
            Asset = ctx.message.author.avatar_url
            imported = Image.open(BytesIO(await Asset.read()))

        imported = imported.resize((148, 172))

        imported = imported.convert('RGB')
        imported.putalpha(255)


        stand = Image.open(self.stand)
        cross = Image.open(self.cross)
        canvas = Image.open(self.canvas)

        cross = cross.resize((157, 188))

        canvas.paste(imported, (52, 75), mask=imported)

        canvas.paste(cross, (47, 77), mask = cross)

        canvas.paste(stand, (0, 0), mask=stand)

        io_object = BytesIO()
        canvas.save(io_object, 'PNG', save_all=True)

        io_object.seek(0)
        await ctx.channel.send(file=discord.File(io_object, 'your_portrait.png'))

    @commands.command(name='counter')
    async def counter(self, ctx):

        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)

        if ctx.message.attachments:
            asset = await ctx.message.attachments[0].read()
            imported = Image.open(BytesIO(asset))

        elif ctx.message.mentions:
            asset = await ctx.message.mentions[0].avatar_url.read()
            imported = Image.open(BytesIO(asset))
        else:
            Asset = ctx.message.author.avatar_url
            imported = Image.open(BytesIO(await Asset.read()))

        base = Image.open(self.thatswrong)

        imported = imported.resize((552, 521))

        imported = imported.convert('RGB')
        imported.putalpha(255)

        base.paste(imported, (775, 238), mask=imported)

        io_object = BytesIO()
        base.save(io_object, 'PNG', save_all=True)

        io_object.seek(0)
        await ctx.channel.send(file=discord.File(io_object, 'counter.png'))

    @commands.command()
    async def gameover(self,ctx):
        self.log(ctx.message.content, ctx.author.name, ctx.guild.name, ctx.channel.name)
        if ctx.message.attachments:
            asset = await ctx.message.attachments[0].read()
            imported = Image.open(BytesIO(asset))
        else:
            Asset = ctx.message.author.avatar_url
            imported = Image.open(BytesIO(await Asset.read()))
        gif = Image.open(self.file_gameover_gif)

        # await save(str(message.author.avatar_url), 'imported', seek_begin=True)
        imported = imported.resize((58, 58))
        imported = imported.convert('RGB')
        imported.putalpha(255)

        frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.copy()
            frame = frame.convert('RGB')

            frames.append(frame)

        for i in range(0, 17):
            frames[i].paste(imported, (215, 102), mask=imported)

        x = 302
        y = 130
        rotated = imported.rotate(270)
        for i in range(17, 36):
            frames[i].paste(rotated, (x, y), mask=rotated)

            if i > 30:
                if i == 34:
                    rotated.putalpha(128)
                elif i == 35:
                    rotated.putalpha(56)
                else:
                    pass

            elif (i % 2) == 0:
                x += 20

        io_object = BytesIO()
        frames[0].save(io_object, 'GIF', save_all=True, append_images=frames[1:])

        io_object.seek(0)
        await ctx.channel.send(file=discord.File(io_object, 'gif file.gif'))



def setup(bot):
    bot.add_cog(ded(bot))