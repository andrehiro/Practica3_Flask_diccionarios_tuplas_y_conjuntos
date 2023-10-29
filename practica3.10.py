from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tupla/<tupla_param1>/<elemento>/')
def eliminarElementoTupla(tupla_param1, elemento):
    tupla = tuple(tupla_param1.split(','))
    if elemento in tupla:
        lista = list(tupla)
        lista.remove(elemento)
        nueva_tupla = tuple(lista)
        return jsonify(nueva_tupla)
    else:
        return jsonify(tupla)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
