from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route('/dict/<diccio>/')
def imprimirTupla(diccio):
    diccionario = json.loads(diccio)
    return diccionario


#http://localhost:5000/dict/{"uno":"1","dos":"2","tres":"3"}
#http://localhost:5000/dict/{"uno",1,2.2,(1,2),"dos"}
