def example1():
    n=100
    def inner():
        m=25
        return n*m
    return inner
x=example1()
print(x())


def counter():
    n=0
    def count():
        nonlocal n
        n+=1
        return n
    return count
a=counter()

print(a())
print(a())
print(a())

