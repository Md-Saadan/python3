x=lambda a,b:a+b
print(x(10,20))
print((lambda a,b:a-b)(10,20))

import math
x=lambda a:math.sqrt(a)+a**2
print(x(25))
print((lambda a:math.sqrt(a)+a**2)(49))

print((lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c))(10,20,30))
print((lambda s:s.upper())("hello"))

n=[110,220,330,440,550,660,770,880,990,1100]
y=lambda n:0 if n%2==0 else 1
print(list(map(y,n)))

print(list(map((lambda n:0 if n%2==0 else 1),[11,22,33,44,55,66,77,88,99,110])))

import math
y=lambda a:math.sqrt(a)-a**3
print(y(16))
print((lambda a:math.sqrt(a)/a**3)(625))
