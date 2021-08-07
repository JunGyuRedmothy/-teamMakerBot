import random
from datetime import datetime
from collections import deque

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Destiny_팀나누기")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await  message.channel.send("안녕하세요")

    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        embed = discord.Embed(title="팀 멤버")
        strSplits = team.split("/")
        teamMember = strSplits[0].split(" ")
        random.shuffle(teamMember)
        dq = deque()
        dq.extend(teamMember)
        teamText= ""
        for i in range(0, int(strSplits[1])):
            for j in range(0, round(len(teamMember)/int(strSplits[1]))):
                if(len(dq) != 0):
                    teamText = teamText+"\t"+dq.popleft()
            embed.add_field(name=str(i+1)+"번 팀", value=teamText, inline=False)
            teamText=""
        embed.set_footer(text="마음에 안들기 없기!!")
        await message.channel.send(embed=embed)
client.run("ODczMTI0OTE2OTA2NTc3OTIw.YQz28g.Ij9QtRwAl7bRpntusNRPVu_hbIQ")

