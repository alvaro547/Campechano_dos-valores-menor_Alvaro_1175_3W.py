print(" ")
print("Alvaro Campechano 3W")
print(" ")
def main():
    # Leer dos valores
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Determinar el menor
    menor = min(num1, num2)
    print(f"El valor menor es: {menor}")

    # Sumar los dos números
    suma = num1 + num2
    print(f"La suma de los dos números es: {suma}")

# Ejecutar el algoritmo
if __name__ == "__main__":
    main()
