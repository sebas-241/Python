print("----- Calculadora -----")
# Operacion a realizar
opcion = int(input("Ingrese la opcion a deseada:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n"))
while opcion <= 0 or opcion > 4:
    opcion = int(input("Ha seleccionado una opcion inexistente. Vuelva a ingresar la opcion a deseada:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n"))
    
# Darle valor a la variable Opcion para que sea mas personalizado
if opcion == 1:
    opcion = "Suma"
elif opcion == 2:
    opcion = "Resta"
elif opcion == 3:
    opcion = "Multiplicacion"
else:
    opcion = "Division"

# Numero de valores a operar. Maximo 5
numerosN = int(input("Cuantos numeros deseas operar (min. 2)(max. 5): "))
while numerosN <= 1 or numerosN > 5:
    numerosN = int(input("Valor Excedido, vuelve a intentarlo. Cuantos numeros deseas operar (max. 5): "))

# Almacenamiento de valores dependiendo el bucle anterior
if numerosN == 2:
    numero1 = int(input(f"Ingresa el primer valor de la {opcion}: "))
    numero2 = int(input(f"Ingresa el segundo valor de la {opcion}: "))
    if opcion == 1 or opcion == 2:
        numero3 = 0
        numero4 = 0
        numero5 = 0
    else:
        numero3 = 1
        numero4 = 1
        numero5 = 1
    
elif numerosN == 3:
    numero1 = int(input(f"Ingresa el primer valor de la {opcion}: "))
    numero2 = int(input(f"Ingresa el segundo valor de la {opcion}: "))
    numero3 = int(input(f"Ingresa el tercer valor de la {opcion}: "))
    if opcion == 1 or opcion == 2:
        numero4 = 0
        numero5 = 0
    else:
        numero4 = 1
        numero5 = 1
        
elif numerosN == 4:
    numero1 = int(input(f"Ingresa el primer valor de la {opcion}: "))
    numero2 = int(input(f"Ingresa el segundo valor de la {opcion}: "))
    numero3 = int(input(f"Ingresa el tercer valor de la {opcion}: "))
    numero4 = int(input(f"Ingresa el cuarto valor de la {opcion}: "))
    if opcion == 1 or opcion == 2:
        numero5 = 0
    else:
        numero5 = 1
        
else:
    numero1 = int(input(f"Ingresa el primer valor de la {opcion}: "))
    numero2 = int(input(f"Ingresa el segundo valor de la {opcion}: "))
    numero3 = int(input(f"Ingresa el tercer valor de la {opcion}: "))
    numero4 = int(input(f"Ingresa el cuarto valor de la {opcion}: "))
    numero5 = int(input(f"Ingresa el quinto valor de la {opcion}: "))

# Funcion que hace las operaciones
def operaciones(opcion, numero1, numero2, numero3, numero4, numero5):
    if(opcion == "Suma"):
        sumaF = numero1 + numero2 + numero3 + numero4 + numero5
        return sumaF
    elif opcion == "Resta":
        restaF = numero1 - numero2 - numero3 - numero4 - numero5
        return restaF
    elif opcion == "Multiplicacion":
        multiF = numero1 * numero2 * numero3 * numero4 * numero5
        return multiF
    else:
        diviF= numero1 // numero2 // numero3 // numero4 // numero5
        return diviF
    
print(operaciones(opcion, numero1, numero2, numero3, numero4, numero5))