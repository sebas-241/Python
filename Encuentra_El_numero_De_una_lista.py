# FOR EN PYTHON
numero_posible = int(input("Ingresa el posible numero que puede esar en la lista: "))
lista = [2, 3, 4, 5, 6, 7, 20, 21]

for n in range(0, len(lista)):
    if(lista[n] == numero_posible):
        resultado = "Has acertado"
        break
    else:
        resultado = "Vuelve a intentarlo"

print(resultado)