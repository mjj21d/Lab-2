#Scatter Plot
import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.linspace(0,2*np.pi,n)
y = np.sin(x)

fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.scatter(x, y, label='simplest')
ax.scatter(x, y - .3, color='b', alpha=np.linspace(0,1,len(x)), label='alpha')
ax.scatter(x, y - .5, c=np.linspace(0,1,len(x)), label='color')
ax.scatter(x, y - .8, s=np.linspace(0,100,len(x)), label='size')
ax.set_title("Scatter")
ax.legend()
plt.show()
