n=int(input("ingrese un numero"))
b=1
f=0
for i in range(1,n):
    if i%2==0:
        a=b
        b=f
        f=a+b
        print(f,",",end='')
    else:
        print("0,0,",end='')                        