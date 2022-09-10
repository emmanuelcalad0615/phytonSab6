
cont2=0
cont3=0
n=int(input("Dígite cuántos número enteros desea ingresar:  "))

enteros=[]

for i in range(n):
    x= int(input("Ingrese un entero: "))
    enteros.append(x)
    
for i in range(n):
    if(enteros[i]%2==0 and enteros[i]%3==0):
        cont2+=1
        cont3+=1
    elif(enteros[i]%3==0):
        cont3+=1
    elif(enteros[i]%2==0 ):
         cont2+=1  
         
    else:
        cont2=0
        cont3=0      

print("La cantidad de números multiplos de 2 es: ", cont2)   
print("La cantidad de números multiplos de 3 es: ", cont3)            
    




    

