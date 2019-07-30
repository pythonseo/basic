import requests
import json
from bs4 import BeautifulSoup
url='https://movie.douban.com/subject/26794435/comments?start=0&limit=20&sort=new_score&status=P&comments_only=1'
response=requests.get(url)
con=json.loads(response.content)
print(type(con))
soup=BeautifulSoup(str(con),'lxml')
print(soup.prettify())
for author,comments in zip(soup.select('a[class='']'),soup.select('span[class="short"]')):
    print(author.get_text(),comments.get_text())
# for comments in soup.select('span[class="short"]'):
#     print(comments.get_text())