from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route('/dict/<tupl>/')
def imprimirTupla(tupl):
    tupla = tuple(tupl.split(','))
    return jsonify(tupla)


#http://localhost:5000/dict/{"uno":"1","dos":"2","tres":"3"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
