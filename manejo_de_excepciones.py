# "2" + 2 --> TypeError
# 3 + hola --> NameError
# while hola --> SyntaxError
# 3/0 --> ZeroDivisionError

#try:
    #Codigo cuestionable
#except: 
    #Este bloque se ejecuta si el try tiene una excepcion
#else:
    #Esto es por si se desea hacer algo mas si en el caso de que el try se ejecute 
    #con exito. Sin excepciones
  
""" divisor = int(input("Ingrese su divisor: "))
dividendo = int(input("Ingrese su dividendo: "))
    
try: 
    division = divisor//dividendo
except ZeroDivisionError:
    print("No puedes dividir entre cero!!!")
    
else:
    print(division)
    
"""


contador = True    #Crear un estado base para el bucle
while contador:             #Definir el bucle
    try:                                                            
        print("Maquina de la suerte. Ganaras o Perderas")           #Estado base
        numero = int(input("Ingrese su numero: "))
    except ValueError:                                              # Si da la excepcion pues mostrar el mensaje y que se devuelva (bucle finito)
        print("Era un numero. Bruto!")  
    else:                                                           #En caso de que pase la excepcion pues con un condicional definir si gano o perdio
        if(numero>10):
            resultado = "Ganaste"
        else:
            resultado = "Perdiste"
        print(resultado)                                # Mostrar el resultado en pantalla    
        contador= False                                    # Cambiar el estado del bucle a False para que deje de ser infinito
