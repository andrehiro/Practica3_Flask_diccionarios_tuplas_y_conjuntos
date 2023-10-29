from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tupla/<tupla_param1>/<tupla_param2>/')
def concatenarTuplas(tupla_param1, tupla_param2):
    tupla1 = tuple(tupla_param1.split(','))
    tupla2 = tuple(tupla_param2.split(','))
    
    nueva_tupla = tupla1 + tupla2

    return jsonify(nueva_tupla)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
