nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))

def promedio_de_notas (n1, n2, n3):
    return (n1+n2+n3)/3

notaF = promedio_de_notas(nota1, nota2, nota3)

if(notaF < 30): # Metodo de calificacion Colombia
    resultado = f"No pasas la materia. Obtuviste un {notaF} en tu nota final."
else:
    resultado = f"Felicitaciones, pasaste la materia con {notaF}"

print(resultado)