'''llave=input('ingrese una clave:\t')
plaintext=input('plaintext:\t')

if len(llave)!=26 and llave==set:
    print(1) #Error
else:
    print(0)#Correcto
#i.isalpha()'''

def codifica(texto):
    desplazamiento=5
    cifrado=""
    if texto==texto.upper():
        lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    else:
        lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    for car in texto:
        if car in lista:
            cifrado += lista[(lista.index(car)+desplazamiento%(len(lista)))]    
        else:
            cifrado+=car
    print(cifrado)
    return cifrado 

def descodifica(texto):
    desplazamiento=5
    decifrado=""
    if texto==texto.upper():
        lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    else:
        lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    for car in texto:
        if car in lista:
            decifrado += lista[(lista.index(car)-desplazamiento%(len(lista)))]    
        else:
            decifrado+=car
    print(decifrado)
    return decifrado 

if __name__=="__main__":
    cifrado=codifica('hola')
    descifrado=descodifica(cifrado)

