import requests

def get_jobs():
  r = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json')
  return r.json()

def show_job(id):
  j = requests.get('https://hacker-news.firebaseio.com/v0/item/{0}.json'.format(id))
  return j.json()

def format_job(job):
  return """

      New {0[type]} Alert

      {0[title]}

      {0[url]}

      ______________________________________

      """.format(job)

def get_all_jobs():
  job_ids = get_jobs()
  full_job_postings = [show_job(job) for job in job_ids]
  return full_job_postings

