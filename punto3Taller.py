print("***Menu***")
print("1. Agregar Producto")
print("2. Mostrar Productos")
print("3. Buscar por Codigo y Editar precio")
print("4. Buscar por Codigo y Eliminar producto")
print("0. Salir")
opcion=100


productos=[]


while(opcion!=0):
    producto={}
    opcion = int(input("Digite una opcion: "))
    if(opcion == 1):
        producto ['Codigo']=int(input("Digite un Codigo: "))
        producto ['Nombre'] = input("Digite el Nombre: ")
        producto ['Precio']=int(input("Digite el Precio: "))
        productos.append(producto)
        
    elif(opcion == 2):
        print(productos)
    elif(opcion == 3):
        codigo = int(input("Digite el Codigo del producto que desea editar"))
        for prod in producto: 
            if( prod['codigo' == codigo]):
               prod['precio'] = float(input('Digite el nuevo precio: '))      
            break
        else:
            print("Producto no encontrado")
    elif(opcion == 4):
        codigo = int(input("Digite el Codigo"))

        for prod in producto:
            if( prod['codigo' == codigo]):
                producto.remove(prod)
            print("Producto eliminado")  
            break  
    elif(opcion == 0):
            break;
    else:
            print("Invalid Opcion");