from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>/<clave>/<valor>/")

def crearDiccionario(diccio,clave,valor):
    diccionario = json.loads(diccio)
    diccionario[clave]= valor
    return diccionario

def show_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#http://localhost:5000/dict/{"uno": "1", "dos": "2", "tres": "3"}