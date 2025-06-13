from te import Te


print("1. Elige el sabor de te (1 = Te negro / 2 = Te Verde / 3 = Agua de hierbas) :")

sabor = int(input("Elige un sabor : "))

print("2. Elige el formato (300 o 500) : ")

formato = int(input("Elige formato : "))


nombre, tiempo, recomendacion = Te.receta(sabor)

precio = Te.obtener_precio(formato)

duracion = Te.duracion

print(f""" 

a. Sabor del tipo de té: {nombre}
b. Formato: {formato}
c. Precio: {precio}
d. Tiempo: {tiempo}
e. Recomendación: {recomendacion}
f. Duracion: {duracion}

""")




