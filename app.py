import os, asyncio, discord

token = os.environ["TOKEN"]
bot = discord.Client()

cusses = []
with open('Cuss.txt', 'r', encoding="utf-8") as f:
    cusses = f.readlines()

for i in range(len(cusses)):
    cusses[i] = cusses[i].replace("\n", "")

print(cusses)

async def bt(games):
    await bot.wait_until_ready()
    while not bot.is_closed():
        for g in games:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(g))

            await asyncio.sleep(5)


@bot.event
async def on_ready():
    print("Loggined as " + bot.user.name)

    ch = 0
    for g in bot.guilds:
        ch += 1

    await bot.change_presence(status=discord.Status.online, activity=await bt(
        [f'{ch}개의 서버에서 사용 ', '욕 필터링']))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.channel.id == 771926827651563520:
        return

    for i in cusses:
        if str(message.content) in i:
            await message.delete()
            await message.author.send("더럽고 추악한 욕쟁이 같으니라고!")
            break

bot.run(token)