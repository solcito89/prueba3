def menu():
    print("\nBienvenido a Automotora Auto seguro")
    print("1. Grabar datos de un automovil")
    print("2. Buscar automovil por patente")
    print("3. Imprimir certificado de vehiculo")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar (1,2,3 o 4): ")
    return opcion

def grabar_auto(autos):
    patente = input("Ingrese la patente del automovil: ")
    marca = input("Ingrese la marca del automovil: ")
    precio = input("Ingrese el valor del automovil: ")
    multas = input("Ingrese la cantidad de multas del automovil: ")
    rut_dueño = input("Ingrese el RUT del dueño del automovil: ")
    nombre_dueño = input("Ingrese el nombre del propietario del auto (nombre completo): ")

    
    
    autos[patente] = {
        'marca': marca,
        'precio': precio,
        'multas': multas,
        'rut_dueño': rut_dueño,
        'nombre_dueño': nombre_dueño
    }
    print("Datos del automovil grabados exitosamente.")

def buscar_auto(autos):
    patente = input("Ingrese la patente del automovil que desea buscar en nuestra base de datos: ")
    if patente in autos:
        print("\nDatos del auto encontrado:")
        print(f"Patente: {patente}")
        print(f"Marca: {autos[patente]['marca']}")
        print(f"Precio: {autos[patente]['precio']}")
        print(f"Multas: {autos[patente]['multas']}")
        print(f"RUT del dueño: {autos[patente]['rut_dueño']}")
        print(f"Nombre del dueño: {autos[patente]['nombre_dueño']}")
    else:
        print("Automovil no encontrado en nuestros archivos.")

def imprimir_certificado(autos):
    patente = input("Ingrese la patente del automovil para imprimir certificado: ")
    if patente in autos:
        print("\nCertificado")
        print("*******************")
        print(f"Nombre del dueño: {autos[patente]['nombre_dueño']}")
        print(f"Marca: {autos[patente]['marca']}")
        print(f"Patente: {patente}")
        print("*******************")
    else:
        print("Automovil no encontrado.")

def main():
    autos = {}
    
    while True:
        opcion = menu()
        
        if opcion == '1':
            grabar_auto(autos)
        elif opcion == '2':
            buscar_auto(autos)
        elif opcion == '3':
            imprimir_certificado(autos)
        elif opcion == '4':
            print("Gracias por utilizar el servicio de Auto seguro. ¡Hasta luego!")
            break
        else:
            print("Esta opcion es invalida")

if __name__ == "__main__":
    main()
