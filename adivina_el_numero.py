import random
numero_cpu = random.randint(0, 10)
numero_user = int(input("Ingrese el numero que posiblemente el computador este pensando: "))

if(numero_cpu == numero_user):
    resultado = f"Has adivinado! El PC estaba pensando en el numero: {numero_cpu} FELICITACIONES"
else:
    resultado = f"Has perdido, el computador estaba pensando en el numero: {numero_cpu} y tu pusiste el numero: {numero_user}"

print(resultado)