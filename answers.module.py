#Lab 2

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
import os

#folder does not exist
def basic_io(path)
  if not os.path.exists(path):
    print("Folder does not exist.")
    return None
#List and sort files
  items = os.listdir(path)
  items.sort()
  types = []

  for item in items:
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path)
      types.append("file")
    else:
      types.append("folder")
      
  

  
                    
