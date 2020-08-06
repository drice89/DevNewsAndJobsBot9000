# get_a_dev_job_discordbot

get_a_dev_job_discordbot is a bot for discord that pulls job postings from from ycombinator and sends them to your server.

## Installation

### requirements
  - Python 3
  - [Requests](https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request)
  - [Discord Py](https://discordpy.readthedocs.io/en/latest/index.html)
  - [Create a bot and invite it to your Discord server](https://discordpy.readthedocs.io/en/latest/discord.html)
 
 Clone the repository

 In your terminal

    cd get_a_dev_job_discordbot
    touch discord_bot_constants.py
    echo 'BOT_CONSTANTS = { "auth_token": "#insert_discord_auth_token_here#"}' >> discord_bot_constants.py

Make sure the prequisites are installed and then run

    python3 discord_bot.py

You should see a message saying

    We have logged in as #bot_name_here#

If you did everything correctly, you will see that your bot is now active on your server

## Commands

  - $hello -> bot will respond with "Hello"
  - $findjob -> bot will respond with most recent job posting from ycombinator
  - $findjobs -> bot will respond with a list of jobs from ycombinator



   
   

