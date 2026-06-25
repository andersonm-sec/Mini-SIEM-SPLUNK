def interprete(recibir_logs):

    lista_logs = []

    for x in recibir_logs:
        partes = x.strip().split("|")

        formato_limpio = []

        for elemento in partes:
            formato_limpio.append(elemento.strip())

        if len(formato_limpio) == 6:
            eventos = {
                "timestamp": formato_limpio[0],
                "tipo de evento": formato_limpio[1],
                "usuario": formato_limpio[2],
                "IP": formato_limpio[3],
                "estado": formato_limpio[4],
                "detalle": formato_limpio[5],
            }

            lista_logs.append(eventos)
    return lista_logs
