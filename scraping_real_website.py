# In this Second part we are going to scrape the data for a real website
# This requires the dependency "requests"
# In you command line hit conda install requests

import requests
from bs4 import BeautifulSoup
import time

# Geting the website we wanna scrape
page_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
page_html = requests.get(page_url)
page_html = page_html.text

# ask user for unfamiliar skill
print("Enter skill you are not familiar with:")
unfamiliar_skill = input(">")
print(f"Filtering out job with {unfamiliar_skill} \n")

# create an instance of BeautifulSoup
soup = BeautifulSoup(page_html, "lxml")

# getting some attibutes for the job posted
def job_description():
    job_cards = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
    for index, job in enumerate(job_cards):
        # if the job was not posted "few" days ago do not scrape
        job_published_date = job.find("span", class_ = "sim-posted").span.text
        if "few" in job_published_date:
            company_name = job.find("h3", "joblist-comp-name").text.replace(" ","")
            job_skill = job.find("span", class_ = "srp-skills").text.replace(" ","")
            # Add the specific link to the job
            # job_link = job.find("header", class_ = "clearfix")
            job_link = job.header.h2.a["href"]
            # let filter out jobs that contains with unfamiliar skills
            if unfamiliar_skill not in job_skill:
                with open(f"job_posted_result/{index}.txt", "w") as f:
                    f.write(f"Company name: {company_name.strip()} \n")
                    f.write(f"Job Skill: {job_skill.strip()} \n")
                    f.write(f"Job_link: {job_link}")
                    print(f"Job saved {index}")
# repeat the process {time_repeat} time
if __name__ == '__main__':
    while True:
        job_description()
        time_repeat = 5
        print(f"waiting {time_repeat} minutes...to get new jobs")
        time.sleep(time_repeat*60)
