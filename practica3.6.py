from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/conjunto/<conjunto_param>/<elemento>/')
def eliminarElementoConjunto(conjunto_param, elemento):
    conjunto = conjunto_param.split(',')
    if elemento in conjunto:
        conjunto.remove(elemento)
        return jsonify(True,conjunto)
    else:
        return jsonify(False,conjunto)

#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
