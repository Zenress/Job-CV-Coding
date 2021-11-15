n = int(input("Type the number "))

def recursiveFactorial(n):
  #Base Part (Condition to stop)
  if n == 1:
    return 1

  #Recursive Part
  return n * recursiveFactorial(n - 1)

print(recursiveFactorial(n))