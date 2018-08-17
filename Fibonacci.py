# Fibonacci Init Function
def initFib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return initFib(n-1) + initFib(n-2)

# Fibonacci Generator Function
def generate(x):
    for i in range(x):
        print(initFib(i+1))