productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]


#El campo disco indica el tipo del disco, es decir, si es mecánico (DD) o de estado sólido
#(SSD).
#También se cuenta con el diccionario “stock”, donde las llaves son el modelo de los notebooks y el valor una lista que incluye el precio y stock del producto. Todos los notebooks
#en el diccionario “productos” aparecen también en el diccionario “stock”. Los puntos
#suspensivos indican que pueden existir muchos más datos. A continuación, se muestra un
#ejemplo del diccionario “stock”:

#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}


def stock_marca(marca):
    count = 0
    for clave, valor in productos.items():
        if valor[0] == marca:
            for key, value in stock.items():
                if key == clave:
                    count += value[1]
    if count >= 1:
        print(f"La cantidad de la marca {marca} en stock es {count}")

def busqueda_precio(p_min, p_max):
    count = 0
    if isinstance(p_min, float) or isinstance(p_max, float):
        return print("Debe ingresar valores enteros")
    else:
        for clave, valor in stock.items():
            if p_min <= valor[0] <= p_max:
                for key, value in productos.items():
                    if key == clave:
                        print(f"{value[0]} - {clave} - ${valor[0]}")
                        count += 1
    if count == 0:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    count = 0
    if modelo in stock:
        for clave, valor in stock.items():
            if clave == modelo:
                valor[0] = p
                print("Precio actualizado!")
                count += 1
                while True:
                    ask = input("Deseas actualizar otro precio? [s/n]").lower()
                    if ask not in ["s", "n"]:
                        print("Introduce una opcion valida!")
                        continue
                    break
                if ask == "s":
                    for key, value in productos.items():
                        for x, y in stock.items():
                            if x == key:
                                print(f"Modelo: {x} - Marca: {value[0]} - Precio: {y[0]}")
                    while True:
                        pregunta = input("Introduce otro modelo a actualizar el precio!").upper()
                        if pregunta not in stock:
                            print("Introduce un modelo valido de la lista!")
                            continue
                        break
                    while True:
                        try:
                            p_new = int(input("Introduce el nuevo precio!"))
                            if isinstance(p_new, int):
                                break
                            else:
                                print("Introduce un precio valido!")
                        except ValueError:
                            print("Introduce un numero entero.")
                    stock[pregunta][0] = p_new
                    print("Precio actualizado!")    
                return True
    else:
        print("El modelo no existe")
        return False
    
def salir():
    print("Programa finalizado")

def menu():
    opcion = 0

    while opcion != 4:
        print("*** MENU PRINCIPAL ***\n1.Stock marca\n2.Busqueda por precio\n3.Actualizar precio\n4.Salir")
        while True:
            try:
                opcion = int(input("Ingrese opcion: "))
                if 1 <= opcion <= 4:
                    break
                else:
                    print("Introduce una opcion vaida")
            except ValueError:
                print("Introduce un valor valido entre [1-4]")

        if opcion == 1:
            while True:
                marquita = input("Introduce la marca a buscar: ")
                if not marquita:
                    print("La marca no puede estar vacia.")
                    continue
                break
            stock_marca(marquita)
        elif opcion == 2:
            while True:
                p1 = int(input("Introduce el valor minimo para buscar!"))
                p2= int(input("Introduce el valor maximo a buscar!"))
                if not p1 or not p2:
                    print("No pueden estar vacios los valores.")
                    continue
                break
            busqueda_precio(p1, p2)
        elif opcion == 3:
            while True:
                modeliyo = input("Introduce el modelo").upper()
                if not modeliyo:
                    print("El texto no puede estar vacio.")
                    continue
                break
            while True:
                try:
                    presio = int(input("Introduce el nuevo precio para ese modelo:"))
                    if isinstance(presio, int):
                        break
                    else:
                        print("Introduce un valor entero")
                except ValueError:
                    print("Introduce un numero entero.")
            actualizar_precio(modeliyo, presio)
        elif opcion == 4:
            salir()


menu()