# Lab-2 Report

#Import my repo on git and input the following for each question.
#input 'python' to run python script

# For Question 1
import numpy as np
import answers_module
answers_module.myrec(5)
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

