import requests
from config import TOKEN_HEC
from config import URL_HEC


def enviar_evento(alerta):

    headers = {
        "Authorization": f"Splunk {TOKEN_HEC}",
        "Content-Type": "application/json",
    }

    payload = {"event": alerta}

    try:

        response = requests.post(
            URL_HEC, headers=headers, json=payload, verify=False, timeout=10
        )
        if response.status_code == 200:
            print("Éxito: Evento enviado correctamente. ✅")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexíon: {e}")
