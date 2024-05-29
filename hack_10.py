"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""
def fn_hack_10(data):
    datos_modificados = []
    numero_incremental = 1
    for item in data:
        nuevo_item = {}
        for valor in item.values():
            nuevo_item[str(numero_incremental)] = str(numero_incremental + 1)
            numero_incremental += 2
        datos_modificados.append(nuevo_item)
    return datos_modificados
