import math

while True:
    print("=== MENÚ ===")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Circunferencia")
    print("4. Salir")
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        lado1 = float(input("Ingresa el lado 1 del triángulo: "))
        lado2 = float(input("Ingresa el lado 2 del triángulo: "))
        lado3 = float(input("Ingresa el lado 3 del triángulo: "))
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print(f"El área del triángulo es: {area}")
        print(f"El perímetro del triángulo es: {perimetro}")

    elif opcion == "2":
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado ** 2
        perimetro = lado * 4
        print(f"El área del cuadrado es: {area}")
        print(f"El perímetro del cuadrado es: {perimetro}")

    elif opcion == "3":
        radio = float(input("Ingresa el radio de la circunferencia: "))
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
        print(f"El área de la circunferencia es: {area}")
        print(f"El perímetro de la circunferencia es: {perimetro}")

    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente de nuevo.")

## EJERCICIO2

    estudiantes = []
continuar = True

while continuar:
    nombre = input("Ingresa el nombre del estudiante: ")
    p1 = float(input("Ingresa la nota de la primera evaluación: "))
    p2 = float(input("Ingresa la nota de la segunda evaluación: "))
    p3 = float(input("Ingresa la nota de la tercera evaluación: "))
    definitiva = (p1 + p2 + p3) / 3
    estudiantes.append((nombre, definitiva))
    respuesta = input("¿Desea ingresar más datos? (YES/NO): ")
    if respuesta == "NO":
        continuar = False

num_aprobados = 0
num_reprobados = 0
promedio_total = 0

for estudiante in estudiantes:
    nombre = estudiante[0]
    definitiva = estudiante[1]
    promedio_total += definitiva

    if definitiva >= 3:
        print(f"{nombre} ha aprobado con una definitiva de {definitiva:.2f}")
        num_aprobados += 1
    else:
        print(f"{nombre} ha reprobado con una definitiva de {definitiva:.2f}")
        num_reprobados += 1

promedio_total /= len(estudiantes)
print(f"\nResumen:")
print(f"Cantidad de aprobados: {num_aprobados}")
print(f"Cantidad de reprobados: {num_reprobados}")
print(f"Promedio total de las definitivas: {promedio_total:.2f}")


#EJERCICIO 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingrese un número: "))

fact = factorial(numero)
print("El factorial de", numero, "es", fact)

num_pares = 0
acum_pares = 0
num_impares = 0
acum_impares = 0

for i in range(1, numero+1):
    if i % 2 == 0:
        num_pares += 1
        acum_pares += i
    else:
        num_impares += 1
        acum_impares += i

print("Cantidad de números pares:", num_pares)
print("Valor acumulado de los pares:", acum_pares)
print("Cantidad de números impares:", num_impares)
print("Valor acumulado de los impares:", acum_impares)

# EJERCICIO 4

# Funciones para realizar las operaciones matemáticas
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

# Función para mostrar el menú y solicitar la opción al usuario
def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Ciclo principal para solicitar los números y realizar operaciones
while True:
    # Solicitar los números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Mostrar el menú y solicitar la opción
    opcion = menu()

    # Realizar la operación seleccionada y mostrar el resultado
    if opcion == 1:
        resultado = sumar(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        resultado = restar(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        resultado = dividir(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == 5:
        print("PROGRAMA CERRADO")
        break
    else:
        print("Opción inválida. Intente de nuevo.")


#EJERCICIO 5 
def ingresar_venta(dia):
    venta = float(input("Ingrese la venta del " + dia + ": "))
    return venta

def menu():
    print("1. Ingresar ventas por día")
    print("2. Mostrar total de ventas")
    print("3. Mostrar promedio de ventas")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

lunes = martes = miercoles = jueves = viernes = sabado = domingo = 0

dias_semana = 0

while True:
    # Mostrar el menú y solicitar la opción
    opcion = menu()

    # Ingresar ventas por día
    if opcion == 1:
        lunes = ingresar_venta("lunes")
        martes = ingresar_venta("martes")
        miercoles = ingresar_venta("miércoles")
        jueves = ingresar_venta("jueves")
        viernes = ingresar_venta("viernes")
        sabado = ingresar_venta("sábado")
        domingo = ingresar_venta("domingo")
        print("Ventas ingresadas exitosamente.")
        dias_semana = 7
    # Mostrar total de ventas
    elif opcion == 2:
        total = lunes + martes + miercoles + jueves + viernes + sabado + domingo
        print("El total de ventas de la semana es:", total)
    # Mostrar promedio de ventas
    elif opcion == 3:
        promedio = (lunes + martes + miercoles + jueves + viernes + sabado + domingo) / dias_semana
        print("El promedio de ventas de la semana es:", promedio)
    # Salir del programa
    elif opcion == 4:
        print("Hasta luego!")
        break
    # Opción inválida
    else:
        print("Opción inválida. Intente de nuevo.")