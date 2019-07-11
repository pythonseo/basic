import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#设置中文字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
movie=['流浪地球','我不是药神','西虹市首富']
tickets=[50,30,20]
#设置中心偏离值
explode = (0,0.11,0)
plt.pie(tickets,labels=movie,explode=explode,colors=['r','g','b'],autopct='%1.1f%%')
plt.legend(loc='upper right',bbox_to_anchor=(0.1,1.0))
plt.title('电影票房及特例')
plt.show()