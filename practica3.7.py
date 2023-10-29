from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/conjunto/<conjunto_param1>/<conjunto_param2>/')
def combinarConjuntos(conjunto_param1, conjunto_param2):
    conjunto1 = set(conjunto_param1.split(','))
    conjunto2 = set(conjunto_param2.split(','))
    
    unionConjuntos = conjunto1.union(conjunto2)
    
    return jsonify(list(unionConjuntos))

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
