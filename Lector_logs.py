from config import RUTA_LOGS


def leer_archivo():
    entrada_informacion = []
    try:
        with open(RUTA_LOGS, "r") as file:
            for x in file:
                entrada_informacion.append(x)
    except FileNotFoundError:
        print("[ERROR] No se pudo encontrar el archivo: registros.logs.txt")

    return entrada_informacion


if __name__ == "__main__":
    leer_archivo()
