import discord
import discord_bot_constants
import ycombinator_api

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    elif message.content.startswith('$findjobs'):
      jobs = ycombinator_api.get_all_jobs()
      for job in jobs:
        if job[url] and job[title]: 
          await message.channel.send(ycombinator_api.format_job(job))

    elif message.content.startswith('$findjob'):
      job = ycombinator_api.get_jobs()[-1]
      job_alert = ycombinator_api.format_job(ycombinator_api.show_job(job))
      await message.channel.send(job_alert)

client.run(discord_bot_constants.BOT_CONSTANTS["auth_token"])
