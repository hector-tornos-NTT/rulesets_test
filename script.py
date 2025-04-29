# script.py

import math, sys, os, random # Error: Importación de módulos no utilizados (sys, os, random)

def calculate_area(radius):
    # Error: Sin manejo de entrada no válida
    area = math.pi * radius ** 2
    return area

def main():
    print("Bienvenido al programa de cálculo de área")
    radio = input("Introduce el radio del círculo: ") # Error: input no convierte el valor a un tipo numérico
    area = calculate_area(radio) # Error: El argumento no es del tipo esperado (str en lugar de float)
    
    print(f"El área del círculo es {area}") # Error: No se maneja el caso en el que el cálculo falle
    
    # Error: Código inalcanzable debido a la salida previa del programa
    if area < 0:
        print("El área no puede ser negativa.")

main() # Error: Falta el guard clause `if __name__ == "__main__":`
