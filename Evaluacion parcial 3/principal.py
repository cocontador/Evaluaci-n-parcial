import funciones as fn
pedidos=[]

while True:
    try:
        print("*******Menú*******")
        print("1. Registrar pedido")
        print("2. Listar los todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcion=int(input("Ingrese una opción: "))
        
        if opcion ==1:
            fn.regitrar_pedidos(pedidos)
        elif opcion==2:
            fn.listar_pedidos(pedidos)
        elif opcion==3:
            fn.imprimir_hoja_ruta(pedidos)
        elif opcion ==4:
            break
        else:
            print("Ingrese una opción válida ")
    
    
    except ValueError:
        print("Debe ingresar un valor numérico")