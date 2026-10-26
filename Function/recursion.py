def febonacii(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        f=febonacii(n-1)+febonacii(n-2)
        # print(febonacii(5))
    return f
for i in range(10):
     print(febonacii(i))

def factorial(n):
    if n==1:
        return 1
    else:
        f=n*factorial(n-1)
        return f
print(factorial(5))


    
