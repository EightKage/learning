import requests
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog"
response = requests.get(url, headers={'user-agent': "hello"})
html = (response.content)
soup = BeautifulSoup(html, 'html.parser')
#a_tags = soup.find_all('a', class_="entry-title-link")
blogs = soup.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()

    blog_datetimr_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetimr_string)
    petty_date = blog_datetime.strftime("%A %b %m %Y")
    print(f"{petty_date} - {title}")


####
# 
# 
# 
# print(titles)





#print(requests.utils.default_headers())