from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tupla/<tupla_param>/')
def revertirTupla(tupla_param):
    tupla = tuple(tupla_param.split(','))

    nueva_tupla = tuple(reversed(tupla))
    
    return jsonify(nueva_tupla)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
