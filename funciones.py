def sumar():
    val1 = int(input("Ingrese primer valor"))
    val2 = int(input("Ingrese segundo valor"))

    resultado = val1 + val2
    print("La suma de los valores es "+str(resultado))


#sumar()


estado_izquierda = input("Vienen autos de la mano izquierda?")
estado_derecha = input("Vienen autos de la mano derecha?")

def cruzar_calle(izq, der):
    resultado = ""
    if(izq and der == "No"):
        resultado = "Puede cruzar la calle"
    else:
        resultado = "No puede cruzar"
    return resultado

print(cruzar_calle(estado_izquierda, estado_derecha))