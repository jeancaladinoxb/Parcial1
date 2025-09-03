def cargar_configuraciones_txt(archivo):
    estados, alfabeto, transiciones, inicial, finales = [], [], {}, None, []
    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith("#") or not linea:
                continue
            if linea.startswith("Estados="):
                estados = linea.split("=")[1].strip().split(",")
            elif linea.startswith("Alfabeto="):
                alfabeto = linea.split("=")[1].strip().split(",")
            elif linea.startswith("Inicial="):
                inicial = linea.split("=")[1].strip()
            elif linea.startswith("Finales="):
                finales = linea.split("=")[1].strip().split(",")
            else:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) == 3:
                    e1, simbolo, e2 = partes
                    transiciones[(e1, simbolo)] = e2
                else:
                    print(f"Línea no reconocida en Conf1.txt: {linea}")

    return estados, alfabeto, transiciones, inicial, finales

def procesar_cadena(cadena, transiciones, inicial, finales):
    estado = inicial
    recorrido = [estado]  
    for simbolo in cadena:
        if (estado, simbolo) in transiciones:
            estado = transiciones[(estado, simbolo)]
            recorrido.append(estado)
        else:
            print(f"Transición no encontrada: ({estado}, {simbolo})")
            return False, recorrido
    return (estado in finales), recorrido

if __name__ == "__main__":
    estados, alfabeto, transiciones, inicial, finales = cargar_configuraciones_txt("Punto1/Conf1.txt")

    with open("Punto1/Cadenas1.txt", "r") as f:
        for linea in f:
            cadena = linea.strip()
            aceptada, recorrido = procesar_cadena(cadena, transiciones, inicial, finales)
            print(f"Cadena: {cadena}")
            print("Recorrido:", " -> ".join(recorrido))
            if aceptada:
                print("Aceptada\n")
            else:
                print("Rechazada\n")