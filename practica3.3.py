from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>/<clave>/<nuevo_valor>")

def modificarValorDiccionario(diccio, clave, nuevo_valor):
    diccionario = json.loads(diccio)
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return diccionario
    else:
        return False

def show_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#http://localhost:5000/dict/{"uno": "1", "dos": "2", "tres": "3"}