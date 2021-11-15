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

print(fibonacci(n))