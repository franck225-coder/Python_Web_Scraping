# In this Second part we are going to scrape the data for a real website
# This requires the dependency "requests"
# In you command line hit conda install requests

import requests

# Making sure the website we wanna scrape is working
page_html = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
print(page_html)