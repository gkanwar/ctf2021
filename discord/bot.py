import asyncio
import asyncpg
import discord
import dotenv
import json
import os

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL')
DBPASS = os.getenv('RCTF_DATABASE_PASSWORD')
DBUSER = 'rctf'
DBNAME = 'rctf'

client = discord.Client()
channel = None

async def log_solve(row):
    print('Team `{row["name"]}` solved challenge `{row["data"]["name"]}`. Congrats!')

async def main():
    conn = await asyncpg.connect(
        host='localhost', user=DBUSER, password=DBPASS, database=DBNAME)
    solves_count = None
    try:
        await conn.set_type_codec('json', encoder=json.dumps, decoder=json.loads, schema='pg_catalog')
        while True:
            print('Checking solves')
            rows = await conn.fetch(
                'SELECT challenges.data, users.name FROM '
                '(solves INNER JOIN challenges ON solves.challengeid=challenges.id) '
                'INNER JOIN users ON solves.userid=users.id')
            # rows = await conn.fetch(f'SELECT * FROM {SOLVE_TABLE}')
            if solves_count is None:
                solves_count = len(rows)
            for new_row in rows[solves_count:]:
                await log_solve(new_row)
            solves_count = len(rows)
            await asyncio.sleep(10)
    finally:
        await conn.close()

@client.event
async def on_ready():
    global channel
    for guild in client.guilds:
        if guild.name == GUILD:
            print(f'{client.user} successfully connected to guild:')
            print(f'{guild.name}(id: {guild.id})')
            channel = discord.utils.get(guild.channels, name=CHANNEL)
            print(f'Found CTF channel: {CHANNEL}(id: {channel.id})')

    # DEBUG:
    # if channel is not None:
    #     await channel.send('Hello, world! [Discord Bot test]')

    await main()

client.run(TOKEN)
