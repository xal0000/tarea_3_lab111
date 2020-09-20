a=int(input("introdusca el primer dato"))
b=int(input("introdusca el segundo dato"))
if a>b:
    aux1=b
    sp1=0
    si1=0
    c1=0
    while aux1>0:
        resto1=aux1%10
        print("el numero menor tiene un digito entero de:  ",resto1)
        c1=c1+1
        if resto1%2==0:
            sp1=sp1+resto1
            aux1=aux1//10
        else:
            si1=si1+resto1
            aux1=aux1//10
    aux2=a
    sp2=0
    si2=0
    c2=0
    while aux2>0:
        resto2=aux2%10
        print("el numero mayor tiene un digito entero de:   ",resto2)
        c2=c2+1
        if resto2%2==0:
            sp2=sp2+resto2
            aux2=aux2//10
        else:
            si2=si2+resto2
            aux2=aux2//10
    ct=c1+c2
    print("hay un tola de :  ",ct,"  de digitos entre los dos numeros")
    spt=sp1+sp2
    sit=si1+si2
    print("la suma de pares de ambos numeros es",spt,"la suma de impares de ambos numeros es: ",sit)
else:
    aux2=a
    sp2=0
    si2=0
    c2=0
    while aux2>0:
        resto2=aux2%10
        print("el numero menor tiene un digito entero de:   ",resto2)
        c2=c2+1
        if resto2%2==0:
            sp2=sp2+resto2
            aux2=aux2//10
        else:
            si2=si2+resto2
            aux2=aux2//10
    aux1=b
    sp1=0
    si1=0
    c1=0
    while aux1>0:
        resto1=aux1%10
        print("el numero mayor tiene un digito entero de:  ",resto1)
        c1=c1+1
        if resto1%2==0:
            sp1=sp1+resto1
            aux1=aux1//10
        else:
            si1=si1+resto1
            aux1=aux1//10
    ct=c1+c2
    print("hay un tola de :  ",ct,"  de digitos entre los dos numeros")
    spt=sp1+sp2
    sit=si1+si2
    print("la suma de pares de ambos numeros es",spt,"la suma de impares de ambos numeros es: ",sit)