#Lab 2

def myrec(x):
# f(x) = 2x - f(x-1), if x>0
# funtion raises exception if x<0
  if x < 0:
    raise Exception("Input must be >= 0)

  if x == 0
    return 0

  return 2*x - myrec(x - 1)
  
                    
