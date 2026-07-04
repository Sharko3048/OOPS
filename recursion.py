def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
countdown(10)

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))