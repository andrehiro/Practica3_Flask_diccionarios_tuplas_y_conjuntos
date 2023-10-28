from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio1>/<path:diccio2>/")

def combinarDiccionarios(diccio1, diccio2):
    diccionario1 = json.loads(diccio1)
    diccionario2 = json.loads(diccio2)
    diccionario = {**diccionario1, **diccionario2}
    return diccionario

def show_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#http://localhost:5000/dict/{"uno": "1", "dos": "2", "tres": "3"}/{"cuatro": "4", "cinco": "5", "seis": "6"}
#http://localhost:5000/dict/{"cuatro": "4", "cinco": "5", "seis": "6"}