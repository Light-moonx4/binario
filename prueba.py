# Lista ordenada y objetivo
numeros = [2, 4, 6, 8, 12, 15, 19, 20, 25]
objetivo = 19

# Pedir al usuario la posición inicial
inicio = int(input(f"Ingresa el índice inicial (0 a {len(numeros)-1}): "))
fin = len(numeros) - 1
encontrado = -1

print(f"\nIniciando búsqueda binaria desde el índice {inicio} hasta {fin}...\n")

while inicio <= fin and encontrado == -1:
    medio = (inicio + fin) // 2
    print(f"Revisando índice {medio}, valor {numeros[medio]}")
    
    if numeros[medio] == objetivo:
        encontrado = medio
    elif numeros[medio] < objetivo:
        inicio = medio + 1
        print(f"Objetivo mayor, mover inicio a {inicio}\n")
    else:
        fin = medio - 1
        print(f"Objetivo menor, mover fin a {fin}\n")

if encontrado != -1:
    print(f"Elemento encontrado en el índice {encontrado}")
else:
    print("Elemento no encontrado")