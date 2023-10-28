from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>/<clave>/")

def eliminarValorDiccionario(diccio,clave) :
    diccionario = json.loads(diccio)
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

def show_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#http://localhost:5000/dict/{"uno": "1", "dos": "2", "tres": "3"}