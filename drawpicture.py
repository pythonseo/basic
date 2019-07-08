import numpy as np
from matplotlib import pyplot as plt
import time
x=np.linspace(-np.pi,np.pi,num=50,endpoint=True)
c,s=np.sin(x),np.cos(x)
plt.plot(x,c)
plt.plot(x,s)
plt.title('sin&cos')
#保存图片
plt.savefig(r'D:\sin.png',dpi=500)
plt.show()
