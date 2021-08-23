##### Scraping our custom html file #########
# Dependencies needed for this project
# BeautifulSoup4 and the parser method will be lxml
# in the command line and hit pip or conda install beautifulsoup4 and lxml

# reading file
with open("local_html_page.html", "r") as html_page:
    content = html_page.read()

# import libraries
from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(content, "lxml")

# returning all h5 tag elements
courses_html_tags = soup.find_all("h5")

# From the tag return the course title
for courses in courses_html_tags:
    courses_title = courses.text
    #print(courses_title)

# Price associated to each course title and description
course_cards = soup.find_all("div", class_="card")
for course in course_cards:
    course_title = course.h5.text
    course_price = course.a.text.split()[-1]
    course_description = course.p.text
    print(f'The course: {course_title} "{course_description}" will cost {course_price}')

