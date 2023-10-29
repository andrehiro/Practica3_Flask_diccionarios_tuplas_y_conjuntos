from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tupla/<tupla_param1>/<elemento>/')
def agregarElementoTupla(tupla_param1, elemento):
    tupla = tuple(tupla_param1.split(','))

    nueva_tupla = tupla + (elemento,)
    return jsonify(nueva_tupla)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
