numeros = [2, 4, 6, 8, 9, 11, 15, 17,19,22,25]
objetivo = int(input("digite el numero que desea encontrar:"))

inicio_usuario = int(input(f"Ingresa el índice inicial (0 a {len(numeros)-1}): "))
inicio_usuario = max(0, min(inicio_usuario, len(numeros)-1))

# AJUSTE: Definimos el rango completo de la lista para que la búsqueda 
# binaria siempre tenga acceso a todos los índices, sin importar el inicio.
inicio = 0 
fin = len(numeros) - 1
encontrado = -1

print(f"\nBuscando el {objetivo} en toda la lista...")

while inicio <= fin:
    medio = (inicio + fin) // 2
    print(f"Revisando índice {medio}, valor {numeros[medio]}")

    if numeros[medio] == objetivo:
        encontrado = medio
        break
    elif numeros[medio] < objetivo:
        inicio = medio + 1
        print(f"Objetivo mayor, moviendo inicio a {inicio}")
    else:
        fin = medio - 1
        print(f"Objetivo menor, moviendo fin a {fin}")

if encontrado != -1:
    print(f"\n¡Logrado! Elemento encontrado en el índice {encontrado}")
else:
    print("\nElemento no encontrado")
