ENERGIA_INICIAL = 18

laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, "I"],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 99, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 99, 2, 99, 1, 99],
    ["F", 1, 3, 1, 1, 1, 99, 1, 1]
]

for i in range(9):
    for j in range(9):
        if laberinto[i][j] == "I":
            inicio = (i, j)
            laberinto[i][j] = 0
        if laberinto[i][j] == "F":
            final = (i, j)
            laberinto[i][j] = 0

ruta = [[0 for _ in range(9)] for _ in range(9)]

movs = [(0, -1), (1, 0), (-1, 0), (0, 1)]

def backtracking(x, y, energia):
    
    if (x, y) == final:
        ruta[x][y] = 1
        return True

    ruta[x][y] = 1

    for dx, dy in movs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 9 and 0 <= ny < 9:

            if laberinto[nx][ny] == 99:
                continue

            if ruta[nx][ny] == 1:
                continue

            costo = laberinto[nx][ny]
            nueva_energia = energia - costo
            
            if costo == 0:
                nueva_energia = energia

            if nueva_energia < 0:
                continue
           
            if backtracking(nx, ny, nueva_energia):
                return True

    ruta[x][y] = 0
    return False


print("LABERINTO ORIGINAL:\n")
for fila in laberinto:
    print(fila)

print("\nBuscando camino...\n")

if backtracking(inicio[0], inicio[1], ENERGIA_INICIAL):
    print("¡Camino encontrado! \n")
else:
    print("No existe un camino \n")

print("MATRIZ DE LA RUTA (recorrido = 1):\n")
for fila in ruta:
    print(fila)
