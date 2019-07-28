import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family = "MicroSoft YaHei", weight = "bold")
year=['2016','2017','2018']
gdp=[4218.04,5223.50,6200]
gdprate=[25.1,24.7,18.98]
x=np.array(year)
y=np.array(gdp)
z=np.array(gdprate)

fig,ax1 = plt.subplots(figsize=(8,5))#创建对象
plt.title('近三年秦皇岛接待游客数及增长率')
plt.xlabel('年份')
plt.ylabel('接待游客数（单位：万人）')
xticks1=list(year)
plt.bar(x,y,width=0.45,align='center',color='c',alpha=0.9)
plt.ylim(0,8000)
plt.xticks(year,xticks1,size='medium')
for a,b in zip(x,y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=7)
ax2=ax1.twinx()#创建双轴
plt.plot(x,z,c='y',marker='o')
plt.ylim(0,30)
plt.ylabel('接待游客数增长率（单位：%）')
for c,d in zip(x,z):
    plt.text(c,d,'{}%'.format(d),ha='center',va='bottom',fontsize=7)

plt.show()
