import discord
import threading
import util.discord_bot_constants as discord_bot_constants
import util.ycombinator_api as ycombinator_api
from discord.ext import tasks

@tasks.loop(hours=1)
async def auto_post_job(message):
    await find_a_job(message, True)

@tasks.loop(minutes=45)
async def auto_post_stories(message):
  hackernews = ycombinator_api.get_top_stories()
  for story in hackernews:
    if not story['id'] in current_stories:
      current_stories.append(story['id'])
      await message.channel.send(ycombinator_api.format_story(story))


client = discord.Client()

current_jobs = []
current_stories = []

async def find_a_job(message, auto=False,):
  job = ycombinator_api.get_jobs()[0]
  if (auto and not job in current_jobs) or not auto:
      current_jobs.append(job)
      job_alert = ycombinator_api.format_story(ycombinator_api.show_story(job))
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
        
Sending any of the following commands will cause the bot to respond in the same channel:

$findjob => last job posted by ycombinator
$findjobs => list of recent jobs posted to ycombinator
$autopostjobs => a background process will post a recent job every hour
$autopoststories => a background process will post top Hackernews stories every 45 min 
$stopjobs => end the auto post loop for jobs
$stopstories => end the autopost loop for stories         
          """)
    
    elif message.content.startswith('$findjobs'):
      await message.channel.send("Getting job list from Ycombinator API. Please wait...")
      jobs = ycombinator_api.get_all_jobs()
      for job in jobs:
        if 'url' in job and 'title' in job: 
          await message.channel.send(ycombinator_api.format_story(job))

    elif message.content.startswith('$findjob'):
      await message.channel.send("Getting last posted job")
      await find_a_job(message)

    elif message.content.startswith('$autopostjobs'):
      await message.channel.send("I will post a new job each hour if available")
      auto_post_job.start(message)

    elif message.content.startswith('$autopoststories'):
      await message.channel.send('I will post new stories every 45 min')
      auto_post_stories.start(message)

    elif message.content.startswith('$stopjobs'):
      await message.channel.send("Stopping the autopost loop - jobs")
      auto_post_job.stop()

    elif message.content.startswith('$stopstories'):
      await message.channel.send("Stopping the autopost loop - stories")
      auto_post_stories.stop()


client.run(discord_bot_constants.BOT_CONSTANTS["auth_token"])



