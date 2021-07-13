
from discord.ext.commands import AutoShardedBot

import discord
from discord.ext import commands
import sys
import datetime
import random
import asyncpg
import psutil, os
import asyncio
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class tenko(commands.AutoShardedBot):

    def log(logmsg):
        print(logmsg)
        sys.stdout.flush()

    async def playing_loop(self):
        await self.wait_until_ready()
        while True:
            await asyncio.sleep(20)
            gamelist = ["hanging out with Himiko!!"]
            title = random.choice(gamelist)
            await self.change_presence(activity=discord.Game(name=title))


    async def on_shard_resumed(self, shard_id):
        print(f'Shard ID {shard_id} has resumed...')

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        print("Username: {0}\nID: {0.id}".format(self.user))

        self.loop.create_task(self.playing_loop())

        process = psutil.Process(os.getpid())
        print(process.memory_info().rss)