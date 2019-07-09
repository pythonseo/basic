import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import pymysql
#定义字体以解决plt图片中文显示乱码问题
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
class Visual(object):
    #定义数据库结构
    def __init__(self,ip,user,password,db,char='utf8'):
        self.ip=ip
        self.user=user
        self.password=password
        self.db=db
        self.char=char
        self.sqlcon=pymysql.connect(
            host=self.ip,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.char
        )
    def getdata(self,sql):
        #数据执行sql语句
        cursors=self.sqlcon.cursor()
        try:
            cursors.execute(sql)
            results=cursors.fetchall()
            return results
        except:
            print('fail')
            self.sqlcon.close()
        self.sqlcon.close()
    def todraw(self,data):
        #数据处理及可视化
        xlist=[]
        ylist=[]
        for datas in data:
            xlist.append(datas[0])
            ylist.append(datas[1])
        print(xlist,ylist)
        x=np.array(xlist)
        y=np.array(ylist)
        plt.plot(x,y)
        plt.title(u'关键词数量分布',fontproperties=font_set)
        plt.xlabel(u'关键词', fontproperties=font_set)
        plt.ylabel(u'出现次数', fontproperties=font_set)
        plt.tick_params(axis='both', labelsize=14)
        #添加数据标签
        for a, b in zip(x, y):
            print(a,b)
            plt.text(a, b + 0.02, '%.0f' % b, ha='center', va='bottom', fontsize=7)
        #保存图片
        # plt.savefig(r'D:\sin.png',dpi=500)
        plt.show()
sqlget=Visual('localhost','root','123456','test',char='utf8')
sql='select title,count(*) from test0 group by title order by count(*) desc'
sqldata=sqlget.getdata(sql)
print(sqldata)
sqlget.todraw(sqldata)


