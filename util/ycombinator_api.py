import requests
from datetime import datetime

def get_jobs():
  r = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json')
  return r.json()

def show_story(id):
  j = requests.get('https://hacker-news.firebaseio.com/v0/item/{0}.json'.format(id))
  return j.json()

def format_story(story):
  date_time = datetime.utcfromtimestamp(story['time']).strftime('%m/%d/%Y %H:%M:%S')
  return """

---------------New {0[type]} Alert---------------
{0[title]}

{0[url]}

Posted at {1}
-------------------------------------------------

      """.format(story, date_time)

def get_all_jobs():
  job_ids = get_jobs()
  full_job_postings = [show_story(job) for job in job_ids]
  return full_job_postings

def get_top_stories():
  top_5_story_ids = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?orderBy="$key"&limitToFirst=5').json()
  hackernews = [show_story(id) for id in top_5_story_ids]
  return hackernews

  
