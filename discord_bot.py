import discord
import threading
import util.discord_bot_constants as discord_bot_constants
import util.ycombinator_api as ycombinator_api
from discord.ext import tasks

@tasks.loop(hours=1)
async def auto_post(message):
    await find_a_job(message, True)

client = discord.Client()

current_jobs = []

async def find_a_job(message, auto=False,):
  job = ycombinator_api.get_jobs()[-1]
  if (auto and not job in current_jobs) or not auto:
      current_jobs.append(job)
      job_alert = ycombinator_api.format_job(ycombinator_api.show_job(job))
      await message.channel.send(job_alert)
  else:
    await message.channel.send('No new jobs')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$help'):
        await message.channel.send("""

$findjob => last job posted by ycombinator
$findjobs => list of recent jobs posted to ycombinator
$autopostjobs => a background process will post a recent job every hour
          
          """)
    
    elif message.content.startswith('$findjobs'):
      await message.channel.send("Getting job list from Ycombinator API. Please wait...")
      jobs = ycombinator_api.get_all_jobs()
      for job in jobs:
        if 'url' in job and 'title' in job: 
          await message.channel.send(ycombinator_api.format_job(job))

    elif message.content.startswith('$findjob'):
      await message.channel.send("Getting last posted job")
      await find_a_job(message)

    elif message.content.startswith('$autopostjobs'):
      await message.channel.send("I will post a new job each hour if available")
      auto_post.start(message)

    elif message.conent.startswith('$stopautopost'):
      await message.chanel.send("Stopping the autopost loop")
      auto_post.stop()



client.run(discord_bot_constants.BOT_CONSTANTS["auth_token"])



