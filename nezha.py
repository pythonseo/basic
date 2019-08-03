import requests
import json
from bs4 import BeautifulSoup
import pymysql
class Nezhacoms(object):
    def __init__(self,ip,user,password,db,charset='utf8'):
        self.ip=ip
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset
        self.sqlcon=pymysql.connect(
            host=self.ip,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset)
    def nezhaspyder(self,url):
        response=requests.get(url)
        con=json.loads(response.content)
        soup=BeautifulSoup(str(con),'lxml')
        for author,comments in zip(soup.select('a[class='']'),soup.select('span[class="short"]')):
            self.nezhastore(str(comments.get_text()),str(author.get_text()))
    def nezhastore(self,c,a):
        cursor=self.sqlcon.cursor()
        sql='insert into test0 set comments="{}",author="{}"'.format(c,a)
        try:
            cursor.execute(sql)
            print('sucess')
            self.sqlcon.commit()
        except Exception as e:
            print(e)
if __name__=='__main__':
    sqlzezha=Nezhacoms('localhost','root','123456','test',charset='utf8')
    url = 'https://movie.douban.com/subject/26794435/comments?start=0&limit=20&sort=new_score&status=P&comments_only=1'
    sqlzezha.nezhaspyder(url)