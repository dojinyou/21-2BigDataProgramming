import requests
from bs4 import BeautifulSoup

def get_soup(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")

  return soup

# stackoverflow
def get_so_jobs(keyword):
  jobs = []
  url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
  soup = get_soup(url)
  jobs_div = soup.find("div",class_="listResults")
  job_list = jobs_div.find_all("div", class_="-job")

  for job_div in job_list :
    job = {}
    job_a = job_div.find("a",class_="s-link")
    job["title"] = job_a["title"]
    job["company"] = job_div.find("h3",class_="fc-black-700").find("span").string
    job["link"] = f'https://stackoverflow.com{job_a["href"]}'
    jobs.append(job)

  return jobs

def get_wwr_jobs(keyword):
  jobs = []
  url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  soup = get_soup(url)
  job_section = soup.find("section",class_="jobs")
  job_list = job_section.find_all("li", class_="feature")
  
  for job_li in job_list :
    job = {}
    job["title"] = job_li.find("span",class_="title").string
    job["company"] = job_li.find("span",class_="company").string
    job["link"] = f'https://weworkremotely.com{job_li.find("a")["href"]}'
    jobs.append(job)

  return jobs

def get_ro_jobs(keyword):
  jobs = []
  url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
  soup = get_soup(url)
  job_table = soup.find("table")
  job_list = job_table.find_all("tr", class_="job")
  
  for job_ in job_list :
    if "closed" not in job_.attrs["class"]:
      job = {}
      job["title"] = job_.find(itemprop="title").string
      job["company"] = job_.find(itemprop="name").string
      job["link"] = f'https://remoteok.io{job_["data-url"]}'
      jobs.append(job)
  
  return jobs