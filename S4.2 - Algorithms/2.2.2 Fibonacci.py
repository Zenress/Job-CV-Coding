n = int(input("Enter the number "))

"""def fibonacci(n):
  #Base case
  if n == 1 or n == 2:
    return 1
  #Recursive case
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(n))"""
FIB_CACHE = {}

def fibonacci(n):
  if n in FIB_CACHE:
    return FIB_CACHE[n]

  #Base case
  if n == 1 or n == 2:
    return 1
  #Recursive case
  else:
    FIB_CACHE[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return FIB_CACHE[n]

"""def fibonacci(n):
  #Base case
  if n <= 2:
    return n
  #Recursive case
  else:    
    return fibonacci(n - 2) + fibonacci(n - 1)"""

"""print(fibonacci(n))"""
if n <= 0:
  print()
else:
  for i in range(n):
    print(fibonacci(i))
