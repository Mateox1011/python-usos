frutas=["manzana","banana","naranja"]
print(frutas[0])
print(frutas[-1])
frutas.append("uva")#agrega un elemento al final de la lista
frutas.insert(1,"pera") #agrega un elemento en la posición especificada, desplazando los elementos posteriores hacia la derecha
frutas.remove("banana")    #elimina el primer elemento que coincida con el valor dado
ultimo=frutas.pop() #elimina el ultimo elemento de la lista y lo devuelve
print("elemento eliminado:",ultimo)
del frutas[0]
