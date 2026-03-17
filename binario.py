numero_lista=[15, 35, 56, 70, 72, 90, 105, 116, 175]
numero_objetivo=175

inicio = 0
fin =len(numero_lista) -1
encontrado=-1

while inicio<= fin and encontrado ==-1:
    medio = (inicio + fin) //2
    if numero_lista[medio] == numero_objetivo:
        encontrado = medio
    elif numero_lista [medio] < numero_objetivo:
        inicio = medio + 1
    else:
        fin = medio -1

if encontrado != -1:
    print("el numero fue encontrado en el indice:",encontrado,"y es",numero_objetivo)
else:
    print("el numero no fue encontrado")