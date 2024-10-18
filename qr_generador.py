def texto_a_binario(texto):
    # Convierte el texto a su representación en binario
    binario = ''.join(format(ord(c), '08b') for c in texto)
    return binario

def agregar_marcadores(matriz, tamano):
    # Agregar los marcadores de posición en las esquinas (Finder Patterns)
    def agregar_cuadrado(matriz, x, y):
        # Cuadrado 7x7
        for i in range(7):
            for j in range(7):
                if i in {0, 6} or j in {0, 6}:
                    matriz[x + i][y + j] = 1  # Borde exterior (negro)
                elif 1 <= i <= 5 and 1 <= j <= 5:
                    if i in {1, 5} or j in {1, 5}:
                        matriz[x + i][y + j] = 0  # Capa blanca interna
                    else:
                        matriz[x + i][y + j] = 1  # Centro negro

    # Agregar marcadores en tres esquinas
    agregar_cuadrado(matriz, 0, 0)  # Esquina superior izquierda
    agregar_cuadrado(matriz, 0, tamano - 7)  # Esquina superior derecha
    agregar_cuadrado(matriz, tamano - 7, 0)  # Esquina inferior izquierda

def agregar_patron_alineacion(matriz, tamano):
    # El patrón de alineación normalmente se encuentra en el centro para ciertos tamaños
    if tamano > 21:
        centro = tamano // 2
        for i in range(-2, 3):
            for j in range(-2, 3):
                matriz[centro + i][centro + j] = 1 if i == 0 or j == 0 else 0

def agregar_patron_timing(matriz, tamano):
    # Patrón de temporización horizontal (fila 6 desde el borde superior, entre los marcadores de posición)
    for i in range(8, tamano - 8):
        matriz[6][i] = i % 2  # Alternar entre negro (1) y blanco (0)
        matriz[i][6] = i % 2  # Patrón de temporización vertical

def agregar_zona_silenciosa(matriz, tamano):
    # Dejar una zona silenciosa (quiet zone) de 4 píxeles alrededor del código QR
    nueva_matriz = [[0 for _ in range(tamano + 8)] for _ in range(tamano + 8)]
    for i in range(tamano):
        for j in range(tamano):
            nueva_matriz[i + 4][j + 4] = matriz[i][j]
    return nueva_matriz

def generar_qr(tamano, texto):
    # Convertimos el texto a binario
    binario = texto_a_binario(texto)
    
    # Crear una matriz vacía (bidimensional) con todos ceros
    matriz = [[0 for _ in range(tamano)] for _ in range(tamano)]
    
    # Agregar los marcadores de posición a la matriz
    agregar_marcadores(matriz, tamano)
    
    # Agregar el patrón de alineación si es necesario (para tamaños más grandes)
    agregar_patron_alineacion(matriz, tamano)

    # Agregar el patrón de temporización
    agregar_patron_timing(matriz, tamano)
    
    # Rellenar la matriz con el binario del texto
    contador_binario = 0
    for i in range(tamano):
        for j in range(tamano):
            # Evitar sobrescribir los patrones de posición, alineación y temporización
            if (matriz[i][j] == 0) and contador_binario < len(binario):
                matriz[i][j] = int(binario[contador_binario])
                contador_binario += 1

    # Agregar la zona silenciosa
    matriz_con_silencio = agregar_zona_silenciosa(matriz, tamano)

    return matriz_con_silencio
