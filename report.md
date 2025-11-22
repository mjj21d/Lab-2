# Lab-2 Report

#Import my repo on git and input the following for each question.
#input 'python' to run python script

# For Question 1
import numpy as np\
import answers_module\
answers_module.myrec(5)\
#The output should be 6.

# For question 2
answers_module.basic_io(".")
#The output would be {'num_items': 7, 'item_names': ['.git', 'Lab-2', '__pycache__', 'answers_module.py', 'line_plot.py', 'report.md', 'scatter_plot.py'], 'item_types': ['folder', 'folder', 'folder', 'file', 'file', 'file', 'file']}

# For question 3
M = np.arange(1,13).reshape(3,4)
answers_module.add2and3(M)
#This would output np.int64(47). The answer is 47

# For question 4
answers_module.squareme(M, 1)
#This would output array([25, 36, 49, 64])

# For question 5
import matplotlib as plt
import line_plot
import scatter_plot
#This would show the line and scatter plots used in the Lab repo


#Line Plot
import matplotlib.pyplot as plt
import numpy as np
#Variables
n = 100
x = np.linspace(0,2*np.pi,n)
y = np.sin(x)

#Plot line
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.set_title('Basic Plot')
ax.plot(x, y, 'r', label='1')
ax.plot(x, y + .5, 'g--', label='2')
ax.set_xlabel("Sopas")
ax.set_ylabel("Pericon")
ax.legend()
plt.show()

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



