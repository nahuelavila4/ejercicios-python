#Tipos de variables
var_texto = 'Hola mundo'

mi_numero = 5
mi_secnum = 100

var_falsa = False
mi_float = 34.766

var_compleja = 3 + 1j
resultado = mi_secnum + mi_numero 

#print("El primer valor es "+ str(resultado))

res = 3 * 'pera' + 'i'
#print(res)

nombre, apellido, alias, edad = "Nahuel", "Avila", "Nano", 22
#print(nombre, apellido, alias, edad)

#Para pedir datos al usuario se usa input, ej:
solicitar_nombre = input("¿Cual es su nombre?")
solicitar_edad = input("¿Cual es su edad?")

#print(solicitar_nombre)
#print(solicitar_edad)

nombre_python = "Python"
print("Usando inicio y fin:" + nombre_python[2:5])
print("Usando solo inicio" + nombre_python[2:]) 
#Toma una porcion de un string. El primer numero es apartir
#de q letra toma, el segundo es hasta que letra toma, no cuenta la letra perteneciente a ese numero
#Tambien se le puede dar solo el primer o el ulti,mo valor

"""
Estructura
<cadena>[inicio:fin]
"""

#Podemos agregarle pasos para decir como queremos rebanar
"""
Estructura
<cadena>[inicio:fin:paso]
"""
print("Usando paso:" + nombre_python[1:6:2])