from pathlib import Path

CARPETA_PROYECTO = Path(__file__).resolve().parent

RUTA_LOGS = CARPETA_PROYECTO / "registros.log.txt"

RUTA_ALERTAS_TXT = CARPETA_PROYECTO / "alertas.txt"

RUTA_ALERTAS_CSV = CARPETA_PROYECTO / "alertasSplunk.csv"


# CONFIGURACION DEL MODULO DE DETECCION

UMBRAL_INTENTOS = 3
UMBRAL_CRITICO = 2
UMBRAL_ADVERTENCIA = 3
MINIMO_DE_EVENTOS = 5
FORMATO = "%Y-%m-%d %H:%M:%S"
LIMITE_DE_SEGUNDOS = 3
ESTADOS_VALIDOS = "SUCCESS", "FAILED"


# CONFIGURACION SPLUNK

HOST_SPLUNK = "localhost"
PUERTO_SPLUNK = 8088

# Reemplazar con el token generado en Splunk HEC
TOKEN_HEC = "AQUI TU TOKEN HEC"

# Url de ejemplo para entorno local
URL_HEC = "https://localhost:8088/services/collector"
