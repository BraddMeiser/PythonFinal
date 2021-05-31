def lista_alumnos(num_alumnos):
    alumnos = []
    for n in range(num_alumnos):
        alumno = {}
        
        alumno['Nombre'] = input('Ingrese el nombre completo: ')
        
        alumnos.append(alumno)
    return alumnos

def notas_alumnos():
    notas=[]
    for n in range(notas):

def promedio(notas):
    for i in lista_alumnos:
        prom=(i['Nota1'] + i['Nota2'] + i['Nota3'])/3
    return prom

num_alumnos = int(input('Introduce la cantidad de alumnos: '))
salon = lista_alumnos(num_alumnos)

print (salon)



