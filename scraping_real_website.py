# In this Second part we are going to scrape the data for a real website
# This requires the dependency "requests"
# In you command line hit conda install requests

import requests
from bs4 import BeautifulSoup

# Geting the website we wanna scrape
page_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
page_html = requests.get(page_url)
page_html = page_html.text

# create an instance of BeautifulSoup
soup = BeautifulSoup(page_html, "lxml")

# getting some attibutes for the job posted
job_cards = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
for job in job_cards:
    # if the job was posted "few" days ago do not scrape
    job_published_date = job.find("span", class_ = "sim-posted").span.text
    if "few" in job_published_date:
        company_name = job.find("h3", "joblist-comp-name").text.replace(" ","")
        job_skill = job.find("span", class_ = "srp-skills").text.replace(" ","")

        print(f'''
            Company name: {company_name}
            Required skill: {job_skill}
            ''')
        print("")