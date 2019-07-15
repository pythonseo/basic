import numpy as np

#ndarray 对象（numpy 数组）

a=np.arange(1,5)
b=np.arange(2,6)
c=a*b
print(c)
print(c.dtype,c.shape)
#创建简单数组
d=np.array([1,2,3])
print(d)
e=np.zeros(2)
print(e)
f=np.ones(3)
print(f)
g=np.empty(3)
print(g)
h=np.eye(3)
print(h)
#创建随机数组
i=np.random.random(5)
print(i)
j=np.random.randint(3,size=(3,2))
print(j)
k=np.random.randint(3,5,size=(3,2))
print(k)
