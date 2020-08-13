def fact(z) :
     if z==0 :
          return 1
     else :
          return z*fact(z-1)
x=input('enter a number')
x=int(x)
y=fact(x)
print(y)
