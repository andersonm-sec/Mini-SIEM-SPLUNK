from datetime import datetime
from config import FORMATO
from config import UMBRAL_INTENTOS
from config import UMBRAL_CRITICO
from config import UMBRAL_ADVERTENCIA
from config import MINIMO_DE_EVENTOS
from config import LIMITE_DE_SEGUNDOS
from config import ESTADOS_VALIDOS


def detectar_actividad(eventos):

    alertas_usuario_ip = validacion_usuario_ip(eventos)
    resultado_tiempo = deteccion_por_tiempo(eventos)

    lista_alertas = alertas_usuario_ip + resultado_tiempo
    return lista_alertas


def deteccion_por_tiempo(eventos):

    contador_tiempos = {}
    alertas_por_tiempo = []

    for evento in eventos:

        tiempo = evento.get("timestamp")
        if not tiempo:
            continue

        if not tiempo.strip():
            continue

        usuario = evento.get("usuario")
        if not usuario:
            continue

        if not usuario.strip():
            continue

        try:

            formato_final = datetime.strptime(tiempo, FORMATO)

        except ValueError:
            print(
                f"Los datos de {tiempo} no coinciden con el formato %Y-%m-%d %H:%M:%S"
            )
            continue

        if usuario not in contador_tiempos:
            contador_tiempos[usuario] = []

        contador_tiempos[usuario].append(formato_final)

        if len(contador_tiempos[usuario]) >= MINIMO_DE_EVENTOS:
            tiempo1 = contador_tiempos[usuario][0]
            tiempo2 = contador_tiempos[usuario][-1]

            diferencia = tiempo2 - tiempo1
            segundos_transcurridos = diferencia.total_seconds()

            conversion_segundos = round(segundos_transcurridos, 2)

            if segundos_transcurridos < LIMITE_DE_SEGUNDOS:
                alertas_por_tiempo.append(
                    f"⚠️ Ataque detectado contra el usuario: {usuario} en un intervalo de {conversion_segundos} segundos."
                )

            if segundos_transcurridos <= UMBRAL_CRITICO:
                alertas_por_tiempo.append(
                    f"🔴  [Riesgo crítico] Usuario: {usuario} realizó una gran cantidad de intentos en {conversion_segundos} segundos."
                )

            elif segundos_transcurridos <= UMBRAL_ADVERTENCIA:
                alertas_por_tiempo.append(
                    f"🟡  [Advertencia] Usuario: {usuario} realizó múltiples intentos en {conversion_segundos} segundos."
                )

    return alertas_por_tiempo


def validacion_usuario_ip(eventos):

    contador_intentos = {}
    contador_ip = {}
    contador_ip_usuarios = {}
    alertas_usuario_ip = []

    for evento in eventos:

        ip = evento.get("IP")
        if not ip:
            continue

        if not ip.strip():
            continue

        estado = evento.get("estado")
        if not estado:
            continue

        if not estado.strip():
            continue

        usuario = evento.get("usuario")
        if not usuario:
            continue

        if not usuario.strip():
            continue

        if usuario not in contador_intentos:
            contador_intentos[usuario] = 0

        if ip not in contador_ip:
            contador_ip[ip] = 0

        if ip not in contador_ip_usuarios:
            contador_ip_usuarios[ip] = set()

        if estado not in ESTADOS_VALIDOS:
            continue

        if estado == "FAILED":
            contador_intentos[usuario] += 1
            contador_ip[ip] += 1
            contador_ip_usuarios[ip].add(usuario)

        elif estado == "SUCCESS":

            if contador_ip[ip] > UMBRAL_INTENTOS:
                alertas_usuario_ip.append(
                    f"⚠️  [POST-LOGIN IP] IP: {ip}, Intentos fallidos desde esta dirección {contador_ip[ip]}"
                )

            if contador_intentos[usuario] > UMBRAL_INTENTOS:
                alertas_usuario_ip.append(
                    f"⚠️  [POST-LOGIN] Usuario: {usuario}, {contador_intentos[usuario]} intentos fallidos antes de iniciar sesión correctamente."
                )

            contador_ip[ip] = 0
            contador_intentos[usuario] = 0

    for ip in contador_ip:
        intentos = contador_ip[ip]

        if intentos > UMBRAL_INTENTOS:
            alertas_usuario_ip.append(
                f"⚠️  [EN CURSO DESDE IP] IP: {ip} con un total de {intentos} intentos fallidos."
            )

    for ip in contador_ip_usuarios:
        cantidad = len(contador_ip_usuarios[ip])

        if cantidad > UMBRAL_INTENTOS:
            alertas_usuario_ip.append(
                f"⚠️  [ATAQUE DISTRIBUIDO] IP: {ip} atacando {cantidad} usuarios distintos."
            )

    for usuario in contador_intentos:
        intentos = contador_intentos[usuario]

        if intentos > UMBRAL_INTENTOS:
            alertas_usuario_ip.append(
                f"⚠️  [EN CURSO] Usuario: {usuario} con un total de {intentos} intentos sin éxito."
            )

    return alertas_usuario_ip
