from Lector_logs import leer_archivo
from interpretar_datos import interprete
from deteccionp import detectar_actividad
from exportar import exportar_alertas_csv
from exportar import exportar_alertas_txt
from transmitir_splunk import enviar_evento


def main():

    print("[INFO] Leyendo logs.....")
    logs = leer_archivo()

    if not logs:
        print("[ALERTA] No se encontraron logs.")
        return

    print("[INFO] Interpretando eventos.....")
    eventos = interprete(logs)

    if not eventos:
        print("[ALERTA] No se encontraron eventos que procesar.")
        return

    print("[INFO] Buscando alertas....")
    alertas = detectar_actividad(eventos)

    if not alertas:
        print("[INFO] No se detectaron amenazas.")
        return

    for alerta in alertas:
        print(alerta)
        enviar_evento(alerta)

    print("[INFO] Exportando resultados.....")
    print(f"[INFO] Total de alertas detectadas: {len(alertas)}")
    exportar_alertas_txt(alertas)
    exportar_alertas_csv(alertas)


if __name__ == "__main__":
    main()
