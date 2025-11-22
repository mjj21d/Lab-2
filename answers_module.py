#Lab 2
import os
import numpy as np

#Question 1

def myrec(x):
# f(x) = 2x - f(x-1), if x>0
# funtion raises exception if x<0
  if x < 0:
    raise Exception("Input must be >= 0")

  if x == 0:
    return 0

  return 2*x - myrec(x - 1)

#Question 2

def basic_io(path):
  #folder does not exist
  if not os.path.exists(path):
    print("Folder does not exist.")
    return None
#List and sort files
  items = os.listdir(path)
  items.sort()
  types = []

  for item in items:
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
      types.append("file")
    else:
      types.append("folder")
#Keys of dictionary
  return {
    "num_items": len(items),
    "item_names": items,
    "item_types": types
  }
      
 #Question 3

def add2and3(matrix):
  arr = np.asarray(matrix)
  #Check if matrix is too small
  if arr.ndim != 2 or arr.shape[0] < 2 or arr. shape[1] < 3:
    print("Matrix too small.")
    return None
  #Add 2nd row and 3rd column
  sum_second_row = arr[1, :].sum()
  sum_third_column = arr[:, 2].sum()
  return sum_second_row + sum_third_column

#Question 4
def squareme(matrix, row):
  arr = np.asarray(matrix)
  #Check row
  if row < 0 or row >= arr.shape[0]:
    print("Row not found.")
    return None

  return np.square(arr[row])
  
    
  


  
                    
