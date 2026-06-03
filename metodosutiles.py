frutas = ["manzana", "banana", "naranja"]
print(frutas[0]) # Primer elemento: 'manzana'
print(frutas[-1]) # Último elemento: 'naranja'
```
### Agregar y eliminar elementos
```python
frutas.append("uva") # Agrega 'uva' al final
frutas.insert(1, "pera") # Inserta 'pera' en la posición 1
print(frutas) # ['manzana', 'pera', 'banana', 'naranja', 'uva']
frutas.remove("banana") # Elimina la primera aparición de 'banana'
ultimo = frutas.pop() # Quita el último elemento ('uva') y lo devuelve
print("Elemento eliminado:", ultimo)
del frutas[0] # Elimina el elemento en la posición 0
numeros=[3,7,3,2,10]
print(numeros.count(3)) #cuenta el numero de veces que aparece el elemento en la lista
print(numeros.index(7)) #devuelve el indice de la primera aparicion del elemento en la lista
numeros.sort() #ordena la lista en orden ascendente 
numeros.reverse() #invierte el orden de los elementos en la lista
copia=numeros.copy() #crea una copia de la lista
numeros.clear() #elimina todos los elementos de la lista
print("numeros:",numeros)  
print("copia:",copia) 
#comprension de listas
cuadrados=[x*x for x in range(5)] #crea una lista de los cuadrados de los numeros del 0 al 9
print(cuadrados)                            
pares=[x for x in range(10) if x%2==0] #crea una lista de los numeros pares del 0 al 9
print(pares)    
impares=[x for x in range(20) if x%2!=0] #crea una lista de los numeros impares del 0 al 9
print(impares) 
puntos=(10,20)
print(puntos[0]) #accede al primer elemento de la tupla
print(puntos[1]) #accede al segundo elemento de la tupla 
x,y=puntos #desempaqueta los elementos de la tupla en variables separadas
print(x,y)
valores=(1,2,2,3,)
print(valores.count(2)) #cuenta el numero de veces que aparece el elemento en el conjunto
print(valores.index(3)) #devuelve el indice de la primera aparicion del elemento  
una=(47,) #tupla de un solo elemento, se necesita la coma para diferenciarla de una variable entre parentesis
print(una)
#set
s={1,2,2,3} #crea un conjunto con los elementos dados, los conjuntos no permiten elementos duplicados
print(s)
s.add(4) #agrega un elemento al conjunto 
s.update([5,6]) #agrega varios elementos al conjunto 
s.remove(2) #elimina un elemento del conjunto, si el elemento no existe se genera un error
s.discard(10) #elimina un elemento del conjunto, si el elemento no existe no se genera un error
print(s)    
#diccionario
persona={"nombre":"ana","edad":25,"ciudad":"Bogotá"}
print(persona["nombre"]) #accede al valor asociado a la clave "nombre"
print(persona.get("correo")) #devuelve el valor asociado a la clave "correo" o None si no existe
persona["correo"]="ana@example.com" #agrega una nueva clave-valor al diccionario
persona["edad"]=26 #modifica el valor asociado a la clave "edad"
persona.update({"pais":"Colombia"}) #agrega una nueva clave-valor al diccionario
del persona["ciudad"] #elimina la clave "ciudad" y su valor asociado 
valor=persona.pop("correo",None) #elimina la clave "correo" y devuelve su valor asociado 
ultimo=persona.popitem() #elimina y devuelve el ultimo par clave-valor agregado al diccionario
print(persona) 

for clave in persona:
    print("clave",clave) #imprime las claves del diccionario
for valor in persona.values():
    print("valor",valor) #imprime los valores del diccionario
for clave,valor in persona.items():
    print(clave,"->",valor) #imprime las claves y valores del diccionario   
persona.clear() #elimina todos los elementos del diccionario
config={"nada":"dev"}
config.setdefault("puerto",8080) #agrega la clave "puerto" con el valor 8080 si no existe, si ya existe devuelve su valor asociado
print(config)
