import pymysql
class Mysql(object):
    def __init__(self,ip,user,password,db,char='utf8'):
        self.ip=ip
        self.user=user
        self.password=password
        self.db=db
        self.char=char
        self.mysqldb=pymysql.connect(
            host=self.ip,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.char)
    def sql_ext(self,sql):
        cursor=self.mysqldb.cursor()
        try:
            cursor.execute(sql)
            self.mysqldb.commit()
            results=cursor.fetchall()
            print(results)
        except:
            print('fail')
            self.mysqldb.close()
        self.mysqldb.close()
testsql=Mysql('localhost','root','123456','test',char='utf8')
sql1='insert into test0 values(12,"top")'
sql2='select * from test0'

testsql.sql_ext(sql1)



