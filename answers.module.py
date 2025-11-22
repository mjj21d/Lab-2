#Lab 2

#Print Test
print("This file is:"_file_)

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

def basic_io(path)
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
    if os.path.isfile(full_path)
      types.append("file")
    else:
      types.append("folder")
#Keys of dictionary
  return {
    "num_items": len(items),
    "item_names": items,
    "item_types": types
  }
      
  

  
                    
