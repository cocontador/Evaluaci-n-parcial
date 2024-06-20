SECTOR=["centro","norte","sur"]

def regitrar_pedidos(pedidos):
    while True: 
        nombre=input("Ingrese nombre y apellido del cliente: ")
        if nombre =="":
            nombre=input("Ingrese nombre y apellido del cliente: ")
        else:
            break
    while True: 
        direccion= input("Ingrese dirección: ")
        if direccion =="":
            direccion= input("Ingrese dirección: ")
        else:
            break
      
    while True:
        sector=input ("Ingrese sector, centro, norte, sur: ").lower
        if sector in SECTOR:
           print("Sector ingresado correctamente")
        elif sector=="":
            sector=input ("Ingrese sector, centro, norte, sur: ").lower
        else:
            break 
   
   
    acumpeq=0
    acummed=0
    acumgra=0
    while True:        
        try:
            print("Tamaño paquete")
            print("1. Pequeño")
            print("2. Mediano")
            print("3. Grande")
            print("4. Salir")
            opctamaño=int(input("Ingrese la opción del tamaño del paquete: "))

            
            if opctamaño!=4:
                cantpaquete=int(input("Ingrese la cantidad de paquetes: "))

            elif opctamaño==1:
                acumpeq=acumpeq+cantpaquete
            elif opctamaño==2:
                acummed=acummed+cantpaquete
            elif opctamaño==3:
                acumgra=acumgra+cantpaquete
            elif opctamaño==4:
                break
            else: 
                print("Salió de la selección de tamaño")
        except ValueError:
            print("Ingrese solo números del 1-4") 
                   

    pedido=[{
    "Nombre": nombre,
    "Direccion":direccion,
    "Sector": sector,
    "Paquetepequeño":acumpeq,
    "Paquetemediano": acummed,
    "Paquetegrande":acumgra
    }]
    
    pedidos.append(pedido)

def listar_pedidos(pedidos):
    for pedido in pedidos:
        if pedido == "":
            imprimir_todo="planilla_todos.txt"
            print(pedido)
               
        else:
            break


def imprimir_hoja_ruta(pedidos):
    nombreArchivo=archivo
    with open (nombreArchivo,"w")as archivo:
      for archivo in nombreArchivo:
       nombreArchivo.write (f"Sector: {pedidos}\n")