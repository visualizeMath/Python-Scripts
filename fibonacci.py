
def fib(n):
   if n==1:return 1
   if n==0:return 0
   return fib(n-1)+fib(n-2)

print("Fibonacci serisi kac elemandan olussun?\n")
a=int(input())
print(fib(a))
