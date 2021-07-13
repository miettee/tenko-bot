from discord.ext import commands
import asyncio
import asyncpg
import json



async def run():
    global bot
    description = ""

    #use your postgres server details here
    credentials = {"user": "", "password": "", "database": "", "host": "127.0.0.1"}
    db = await asyncpg.create_pool(**credentials)


    #this whole section is essentially duct taped together, theres definitely a better way to deal with postgres discord intergration, but it's worked so far lol

    await db.execute("CREATE TABLE IF NOT EXISTS newvibedata(userid BIGINT PRIMARY KEY, vibecount INT, vibepoints INT, viberesets INT);")
    await db.execute(
        "CREATE TABLE IF NOT EXISTS times(userid BIGINT PRIMARY KEY, vibecooldown BIGINT, askcooldown BIGINT);")
    await db.execute(
        "CREATE TABLE IF NOT EXISTS votes(userid BIGINT PRIMARY KEY, voted TEXT);")
    await db.execute(
        "CREATE TABLE IF NOT EXISTS customise(userid BIGINT PRIMARY KEY, toptext TEXT, bottomtext TEXT);")
    bot = Bot(description=description, db=db, command_prefix="cb.")

    #this makes all your tables, you don't need to set anything up manually


class Bot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(
            description=kwargs.pop("description"), command_prefix="cb."
        )
        self.db = kwargs.pop("db")


    async def query(self, userid):
        query = "SELECT * FROM newvibedata WHERE userid = $1;"

        row = await bot.db.fetchrow(query, userid)
        return row


    async def querycustom(self, userid):
        query = "SELECT * FROM customise WHERE userid = $1;"

        row = await bot.db.fetchrow(query, userid)
        return row


    async def updatecustom(self, userid, type, text):
        if type == "top":
            column = "toptext"
        elif type == "bottom":
            column = "bottomtext"
        else:
            return
        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"UPDATE customise " \
                    f"SET {column} = $2" \
                    f" WHERE userid = $1;"
            await bot.db.execute(query, userid, text)
        await bot.db.release(connection)

    async def addtocustom(self, userid):
        connection = await bot.db.acquire()



        async with connection.transaction():
            query = f"INSERT INTO customise(userid, toptext, bottomtext) VALUES ($1, 'Put your custom top text here!','Put your custom bottom text here!');"
            await bot.db.execute(query, userid)
        await bot.db.release(connection)


    async def check(self, userid):
        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"select exists(select * from newvibedata where userid=$1);"
        await bot.db.release(connection)
    async def checkvoted(self, userid):
        query = "SELECT * FROM votes WHERE userid = $1;"

        row = await bot.db.fetchrow(query, userid)

        return row

    async def addvoted(selfself, userid, votestatus):
        connection = await bot.db.acquire()

        query = "SELECT * FROM votes WHERE userid = $1;"

        row = await bot.db.fetchrow(query, userid)

        if not row:
            async with connection.transaction():
                query = f"INSERT INTO votes(userid, voted) VALUES ($1, $2);"
                await bot.db.execute(query, userid, votestatus)
            await bot.db.release(connection)
        else:
            async with connection.transaction():
                query = f"UPDATE votes " \
                        f"SET voted = $2" \
                        f" WHERE userid = $1;"
                await bot.db.execute(query, userid, votestatus)
            await bot.db.release(connection)


    async def add(self, userid, vibecount, vibepoints, viberesets):
        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"INSERT INTO newvibedata(userid, vibecount, vibepoints, viberesets) VALUES ($1, $2, $3, $4);"
            await bot.db.execute(query, userid, vibecount, vibepoints, viberesets)
        await bot.db.release(connection)
    async def update(self, userid, vibecount, vibepoints, viberesets):

        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"UPDATE newvibedata " \
                    f"SET vibecount = $2," \
                    f"vibepoints = $3," \
                    f"viberesets = $4" \
                    f" WHERE userid = $1;"
            await bot.db.execute(query, userid, vibecount, vibepoints, viberesets)
        await bot.db.release(connection)

    async def update_value(self, userid, new_row):

        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"UPDATE newvibedata SET data = $1 WHERE userid = $2"
            await bot.db.execute(query, json.dumps(new_row), userid)
        await bot.db.release(connection)

    async def querytime(self, userid):
        query = "SELECT * FROM times WHERE userid = $1;"

        row = await bot.db.fetchrow(query, userid)
        return row

    async def updatetime(self, userid, type, epoch):
        if type == "vibe":
            column = "vibecooldown"
        elif type == "ask":
            column = "askcooldown"
        else:
            return
        connection = await bot.db.acquire()
        async with connection.transaction():
            query = f"UPDATE times " \
                    f"SET {column} = $2" \
                    f" WHERE userid = $1;"
            await bot.db.execute(query, userid, epoch)
        await bot.db.release(connection)

    async def addtotimes(self, userid):
        connection = await bot.db.acquire()

        async with connection.transaction():
            query = f"INSERT INTO times(userid, vibecooldown, askcooldown) VALUES ($1, 0,0);"
            await bot.db.execute(query, userid)
        await bot.db.release(connection)


    async def order(self, userid):

        connection = await bot.db.acquire()

        async with connection.transaction():
            query = "select userid, vibepoints from newvibedata order by vibepoints desc;"
            await bot.db.execute(query)
        await bot.db.release(connection)

        row = await bot.db.fetch(query)

        position = list(dict(row).keys()).index(userid)

        row = list(row)

        total = len(row)
        row = row[:20]

        points = []
        people = []

        for i in range(0, len(row)):
            row[i] = dict(row[i])
            people.append(row[i].get("userid"))
            points.append(row[i].get("vibepoints"))



        await bot.close()
        return people, points, position, total


loop = asyncio.get_event_loop()
loop.run_until_complete(run())