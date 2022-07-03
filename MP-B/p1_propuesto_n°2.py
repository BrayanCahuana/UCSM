a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range (a, b+1):
    suma = suma + i
print("La suma es: ", suma)