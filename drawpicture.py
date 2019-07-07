import numpy as np
from matplotlib import pyplot as plt
x=np.array([1,2,3])
y=x*2
plt.title('demo')
plt.xlabel('x')
plt.ylabel('y')
plt.bar(x,y,color='y')
plt.show()