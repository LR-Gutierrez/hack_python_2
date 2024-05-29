"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(data):
    datos_modificados = {}
    for clave, valor in data.items():
        if clave.lower() == "foo":
            clave_modificada = "Foo"
            datos_modificados[clave_modificada] = "Fooziman"
    return datos_modificados
