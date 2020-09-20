s=0
a=int(input("ingrese el primer dato para realizar la multiplicacion mediante sumas sucesivas:  "))
b=int(input("ingrese el segundo dato para realizar la multiplicacion mediante sumas sucesivas:  "))
if b>0:
    for i in range(b):
        s=a+s
        print(s)
elif b<0 and a>0:
    
    for i in range(a):
        s=s+b
        print(s)

elif a<0 and b<0:

    for i in range(-b):
        s=s-a
        print(s)

