from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tupla/<tupla_param>/')
def imprimirTupla(tupla_param):
    tupla = tuple(tupla_param.split(','))
    return jsonify(tupla)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
