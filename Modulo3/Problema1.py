def validcard(N):
    T=""; par=0;impar=0;X=""
    if not N.isdigit():return 1,""
    if len(N) <14 or len(N)> 17: return 2,""

    for c in range(0,len(N),2):
        X=str(int(N[c])*2)
        if len(X)==2:
            par+=(int(X[0]) + int(X[1]))
        else:
            par+=int(X)

    for c in range(1,len(N),2):
        impar+=int(N[c])

    if (par+impar)%10!=0:return 3,""
    if int(N[0:2])>49 and int(N[0:2])<56:T="**MasterCard**"
    if N[0:2]=="34" or N[0:2]=="37":T="**America Express**"
    if N[0]=="4":T="**VISA**"
    return 4,T

msg=(0,"")
while msg[0]!=4:
    msg=validcard(input("Ingrese su numero de tarjeta: "))
    if msg[0]==1 : print("error!! solo numeros del 0 al 9")
    if msg[0]==2 : print("debe tener 13 o mas(menos o igual a 16)")
    if msg[0]==3 : print("Numero Invalido!!!")

print("Es Valida su tarjeta!!!!")
print("Type: "+msg[1])