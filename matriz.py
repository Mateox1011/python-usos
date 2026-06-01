matriz=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matriz[0]
matriz[1][2] 
for i in matriz:
    print(i) 
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()
matriz[1][1]=99
print(matriz)
filas=3
columnas=4
matriz2=[[0 for j in range(columnas)] for i in range(filas)]
print(matriz2)
#Crear una matriz con valores ingresados por el usuario
filas=int(input("Ingrese el número de filas: "))
columnas=int(input("Ingrese el número de columnas: "))
matriz3=[[0 for j in range(columnas)] for i in range(filas)]
'''
for i in range(filas):
    for j in range(columnas):
        matriz3[i][j]=int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
'''

matriz3=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz3.append(fila)

print("Matriz ingresada:")
for fila in matriz3:
    print(fila)
"""
funciones y gestión de archivos"""
def sumar(a,b):
    resultado =a+b
    return resultado
x=3
y=5
s=sumar(x,y) #almacena el resultado de la función sumar en la variable s
print(f"La suma de {x} y {y} es: {s}",s)
print(sumar(10,20)) 
print(sumar(2,3))
print(sumar("Hola, ","mundo!"))
def saludar():
    print("¡Hola! Bienvenido a la programación con funciones.")
    return saludar()
print(saludar())

def mostrar_mayor(a,b): 
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))       
    if b > a:
        return b
        print("mayor es", b)
    elif a > b:
        return a
        print("mayor es", a)
    else:
        print("Ambos números son iguales")  

def saludar(nombre, saludo="hola"):
    print(saludo, nombre)
saludar("Juan")
saludar("María", "¡Buenos días!")

