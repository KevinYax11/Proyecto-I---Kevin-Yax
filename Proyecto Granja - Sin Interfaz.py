import random
import time

cultivos = {
    'trigo': {'etapas': 4, 'productos': ['granos de trigo'], 'tiempo_cosecha': 0.5, 'rendimiento': 5},
    'maíz': {'etapas': 4, 'productos': ['mazorcas de maíz'], 'tiempo_cosecha': 1, 'rendimiento': 6},
    'zanahorias': {'etapas': 3, 'productos': ['zanahorias'], 'tiempo_cosecha': 0.5, 'rendimiento': 4},
    'manzanas': {'etapas': 5, 'productos': ['manzanas'], 'tiempo_cosecha': 1, 'rendimiento': 8},
    'uvas': {'etapas': 5, 'productos': ['racimos de uvas'], 'tiempo_cosecha': 1, 'rendimiento': 9}
}


animales = {
    'vaca': {'salud': 100, 'hambre': 0, 'felicidad': 100, 'produccion': ['leche'], 'tiempo_produccion': 3, 'rendimiento': 5},
    'oveja': {'salud': 100, 'hambre': 0, 'felicidad': 100, 'produccion': ['lana'], 'tiempo_produccion': 3, 'rendimiento': 4},
    'pollo': {'salud': 100, 'hambre': 0, 'felicidad': 100, 'produccion': ['huevos'], 'tiempo_produccion': 2, 'rendimiento': 3}
}

campo = []
granja = []

dinero = 1000

precios_productos = {
    'granos de trigo': 5,
    'mazorcas de maíz': 8,
    'zanahorias': 7,
    'manzanas': 10,
    'racimos de uvas': 12,
    'leche': 15,
    'lana': 20,
    'huevos': 6
}

def plantar_cultivo(cultivo):
    campo.append({'cultivo': cultivo, 'etapa': 0})

def anadir_animal(animal):
    granja.append({'animal': animal, 'dias_sin_comer': 0, 'dias_sin_acariciar': 0})

def avanzar_dia():
    for cultivo in campo:
        # Aumentar la etapa de crecimiento del cultivo en lugar de avanzar un día
        cultivo['etapa'] += 1

    for animal in granja:
        animal['dias_sin_comer'] += 1
        animal['dias_sin_acariciar'] += 1


def mostrar_estado_cultivos():
    for cultivo in campo:
        if cultivo['etapa'] == cultivos[cultivo['cultivo']]['etapas'] - 1:
            print(f"{cultivo['cultivo']} está maduro y listo para cosechar.")
        else:
            print(f"{cultivo['cultivo']} está en la etapa {cultivo['etapa']} de {cultivos[cultivo['cultivo']]['etapas']}.")

def mostrar_estado_animales():
    for animal in granja:
        animal_info = animales[animal['animal']]
        if animal_info['salud'] <= 0:
            print(f"{animal['animal']} ha muerto.")
            granja.remove(animal)
        elif animal_info['salud'] < 40:
            print(f"{animal['animal']} está enfermo y necesita atención médica.")
        elif animal_info['salud'] < 80:
            print(f"{animal['animal']} no se siente muy bien.")
        else:
            print(f"{animal['animal']} está saludable.")

def recolectar_recursos():
    recursos_obtenidos = []
    for animal in granja:
        animal_info = animales[animal['animal']]
        if animal_info['produccion']:
            productos = [animal_info['produccion'][0]] * animal_info['rendimiento']
            recursos_obtenidos.extend(productos)
    return recursos_obtenidos

def comprar_productos():
    global dinero
    print("Productos disponibles para comprar:")
    for producto, precio in precios_productos.items():
        print(f"{producto} - Precio: Q{precio}")
    producto_comprar = input("Elige un producto para comprar o escribe 'salir' para volver: ").lower()
    if producto_comprar in precios_productos:
        precio_producto = precios_productos[producto_comprar]
        if dinero >= precio_producto:
            dinero -= precio_producto
            print(f"Has comprado {producto_comprar} por Q{precio_producto}.")
            return producto_comprar
        else:
            print("No tienes suficiente dinero para comprar este producto.")
    elif producto_comprar == 'salir':
        return None
    else:
        print("Producto no válido.")
    return None

def vender_productos():
    global dinero
    print("Tus productos disponibles para vender:")
    for producto, cantidad in inventario_productos.items():
        print(f"{producto} - Cantidad: {cantidad}")
    producto_vender = input("Elige un producto para vender o escribe 'salir' para volver: ").lower()
    if producto_vender in inventario_productos:
        precio_producto = precios_productos[producto_vender]
        cantidad_producto = inventario_productos[producto_vender]
        dinero += precio_producto * cantidad_producto
        print(f"Has vendido {cantidad_producto} unidades de {producto_vender} por Q{precio_producto * cantidad_producto}.")
        inventario_productos[producto_vender] = 0
    elif producto_vender == 'salir':
        return None
    else:
        print("Producto no válido.")
    return None

def menu_mercado():
    global dinero
    while True:
        print("Bienvenido al Mercado de la Granja")
        print(f"Dinero disponible: Q{dinero}")
        print("1. Comprar productos")
        print("2. Vender productos")
        print("3. Comprar mejoras")
        print("4. Salir del Mercado")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            producto_comprado = comprar_productos()
            if producto_comprado:
                if producto_comprado in inventario_productos:
                    inventario_productos[producto_comprado] += 1
                else:
                    inventario_productos[producto_comprado] = 1
        elif opcion == '2':
            producto_vendido = vender_productos()
        elif opcion == '3':
            comprar_mejoras()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def comprar_mejoras():
    global dinero
    print("Mejoras disponibles para comprar:")
    mejoras = {
        'Máquina de riego': {'precio': 500, 'mejora_cultivos': 1, 'mejora_animales': 0},
        'Establo ampliado': {'precio': 800, 'mejora_cultivos': 0, 'mejora_animales': 1},
        'Invernadero': {'precio': 1000, 'mejora_cultivos': 2, 'mejora_animales': 0}
    }
    for mejora, datos in mejoras.items():
        print(f"{mejora} - Precio: Q{datos['precio']} - Mejora de cultivos: {datos['mejora_cultivos']} - Mejora de animales: {datos['mejora_animales']}")
    mejora_comprar = input("Elige una mejora para comprar o escribe 'salir' para volver: ").lower()
    if mejora_comprar in mejoras:
        precio_mejora = mejoras[mejora_comprar]['precio']
        if dinero >= precio_mejora:
            dinero -= precio_mejora
            print(f"Has comprado la mejora {mejora_comprar} por Q{precio_mejora}.")
        else:
            print("No tienes suficiente dinero para comprar esta mejora.")
    elif mejora_comprar == 'salir':
        return None
    else:
        print("Mejora no válida.")
    return None

def menu_principal():
    global dinero
    while True:
        print("Bienvenido a tu Granja")
        print(f"Dinero disponible: Q{dinero}")
        print("1. Realizar actividades diarias")
        print("2. Visitar el Mercado de la Granja")
        print("3. Salir de la Granja")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            realizar_actividades_diarias()
        elif opcion == '2':
            menu_mercado()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


cultivos_regados = []  # Lista para rastrear los cultivos regados en el día actual

def regar_cultivos():
    if not campo:
        print("No tienes cultivos plantados. ¡Planta primero!")
        return

    print("Elige un cultivo para regar:")
    for i, cultivo in enumerate(campo, 1):
        if cultivo not in cultivos_regados:
            print(f"{i}. {cultivo['cultivo']}")
    eleccion = input("Opción: ")
    if eleccion.isdigit():
        eleccion = int(eleccion)
        if 1 <= eleccion <= len(campo):
            cultivo_seleccionado = campo[eleccion - 1]
            if cultivo_seleccionado not in cultivos_regados:
                cultivos_regados.append(cultivo_seleccionado)
                print(f"Has regado {cultivo_seleccionado['cultivo']} exitosamente.")
            else:
                print(f"{cultivo_seleccionado['cultivo']} ya ha sido regado hoy.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")



def alimentar_animales():
    for animal in granja:
        animal_info = animales[animal['animal']]
        if animal_info['hambre'] < 50:
            animal_info['hambre'] = 0
        else:
            animal_info['hambre'] -= 50

def acariciar_animales():
    for animal in granja:
        animal_info = animales[animal['animal']]
        animal_info['felicidad'] += 10

def cuidar_animales():
    for animal in granja:
        animal_info = animales[animal['animal']]
        if animal_info['salud'] < 80:
            animal_info['salud'] += 20

def recoger_recursos_animales():
    recursos_obtenidos = recolectar_recursos()
    if recursos_obtenidos:
        for recurso in recursos_obtenidos:
            if recurso in inventario_productos:
                inventario_productos[recurso] += 1
            else:
                inventario_productos[recurso] = 1
    else:
        print("No hay recursos para recolectar de los animales.")



def recoger_cosechas():
    global dinero
    productos_recolectados = []

    for cultivo in campo:
        if cultivo['etapa'] == cultivos[cultivo['cultivo']]['etapas'] - 1:
            cultivo_info = cultivos[cultivo['cultivo']]
            productos_recolectados.extend(cultivo_info['productos'])
            campo.remove(cultivo)

    if productos_recolectados:
        for producto in productos_recolectados:
            if producto in inventario_productos:
                inventario_productos[producto] += 1
            else:
                inventario_productos[producto] = 1

        print("Has recolectado los productos de los cultivos maduros.")


def realizar_actividades_diarias():
    global dinero
    cultivos_regados.clear()  # Limpiar la lista de cultivos regados al comienzo del día

    for dia in range(1, 11):
        print(f"Día {dia}:")

        decision = input("¿Qué deseas hacer hoy?\n"
                         "1. Plantar cultivos\n"
                         "2. Regar cultivos\n"
                         "3. Añadir animal a la granja\n"
                         "4. Alimentar animales\n"
                         "5. Acariciar animales\n"
                         "6. Cuidar animales\n"
                         "7. Recoger recursos de animales\n"
                         "8. Recoger Cosechas\n"
                         "9. Avanzar al siguiente día\n"
                         "10. Terminar\n"
                         "Elige una opción: ").lower()

        if decision == '1':
            plantar_cultivo_menu()
        elif decision == '2':
            regar_cultivos()
        elif decision == '3':
            anadir_animal_menu()
        elif decision == '4':
            alimentar_animales()
            print("Has alimentado a los animales.")
        elif decision == '5':
            acariciar_animales()
            print("Has acariciado a los animales.")
        elif decision == '6':
            cuidar_animales()
            print("Has cuidado a los animales.")
        elif decision == '7':
            recoger_recursos_animales()
            print("Has recolectado los productos de los animales.")
        elif decision == '8':
            recoger_cosechas()
        elif decision == '9':
            avanzar_dia()
            mostrar_estado_cultivos()
            mostrar_estado_animales()
        elif decision == '10':
            break


        mostrar_estado_cultivos()
        mostrar_estado_animales()

        if decision == '4':
            print("Has alimentado a los animales.")
        elif decision == '5':
            print("Has acariciado a los animales.")
        elif decision == '6':
            print("Has cuidado a los animales.")
        elif decision == '7':
            print("Has recolectado los productos de los animales.")
        elif decision == '8':
            print("Has avanzado al siguiente día.")
        print()  # Agregamos línea en blanco para separar acciones



        if decision == '1':
            plantar_cultivo_menu()
        elif decision == '2':
            regar_cultivos()
        elif decision == '3':
            anadir_animal_menu()
        elif decision == '4':
            alimentar_animales()
        elif decision == '5':
            acariciar_animales()
        elif decision == '6':
            cuidar_animales()
        elif decision == '7':
            recoger_recursos_animales()
        elif decision == '8':
            avanzar_dia()
        elif decision == '9':
            break

        mostrar_estado_cultivos()
        mostrar_estado_animales()

        if decision == '4':
            print("Has alimentado a los animales.")
        elif decision == '5':
            print("Has acariciado a los animales.")
        elif decision == '6':
            print("Has cuidado a los animales.")
        elif decision == '7':
            print("Has recolectado los productos de los animales.")
        elif decision == '8':
            print("Has avanzado al siguiente día.")
        print()  # Agregamos línea en blanco para separar acciones

inventario_productos = {}

def plantar_cultivo_menu():
    print("Elige un cultivo para plantar:")
    for i, cultivo in enumerate(cultivos.keys(), 1):
        print(f"{i}. {cultivo}")
    eleccion = input("Opción: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(cultivos):
        opciones = list(cultivos.keys())
        plantar_cultivo(opciones[int(eleccion) - 1])
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def anadir_animal_menu():
    print("Elige un animal para añadir a tu granja:")
    for i, animal in enumerate(animales.keys(), 1):
        print(f"{i}. {animal}")
    eleccion = input("Opción: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(animales):
        opciones = list(animales.keys())
        anadir_animal(opciones[int(eleccion) - 1])
    else:
        print("Opción no válida. Inténtalo de nuevo.")

menu_principal()
