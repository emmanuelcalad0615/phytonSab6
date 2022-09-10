
listaFrutas=[]

for i in range(2):
    fruta={'nombre':input('Ingrese el nombre de la fruta: '), 'color':input('Ingrese el color de la fruta: '), 'precio':input("Ingrese el precio de la fruta: ")}
    listaFrutas.append(fruta)

listaFrutas.reverse()
print(listaFrutas)    


