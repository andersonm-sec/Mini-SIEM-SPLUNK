from config import RUTA_ALERTAS_TXT
from config import RUTA_ALERTAS_CSV
import csv


def exportar_alertas_txt(lista_alertas):
    try:
        with open(RUTA_ALERTAS_TXT, "w", encoding="utf-8") as archivo:
            for alerta in lista_alertas:
                archivo.write(f"{alerta}\n")
    except PermissionError:
        print(
            "[ERROR CRITICO] No existen permisos de escritura para ejecutar esta acción"
        )
    except OSError:
        print("[ERROR] Ocurrió un problema al guardar el archivo de alertas.")


def exportar_alertas_csv(lista_alertas):

    try:

        with open(
            RUTA_ALERTAS_CSV,
            "w",
            newline="",
            encoding="utf-8",
        ) as archivo:

            escritor = csv.writer(archivo)
            escritor.writerow(["Alerta"])

            for alerta in lista_alertas:
                escritor.writerow([alerta])

            print("CSV Generado exitosamente ✅")
    except PermissionError:
        print("[ERROR] El archivo no puede ser modificado en este momento.")
    except OSError:
        print("[ERROR] Ocurrió un problema al guardar el archivo de alertas.")
