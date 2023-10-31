# Practica3_Flask_diccionarios_tuplas_y_conjuntos
Andre Alexander Hidrogo Rocha 31/10/2023 Uso de parametros por medio de rutas en flask

Para lograr la implementación de esta práctica primero es necesario crear un ambiente y descargar Flask. 
Puedes usar los siguientes comandos para realizarlo:

python -m venv venv

source venv/bin/activate  # En sistemas UNIX
venv\Scripts\activate  # En sistemas Windows

pip install Flask

Para implementar el uso de parametros en la ruta tenemos que hacer lo siguiente:

```python
from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>/<clave>/<nuevo_valor>")

def modificarValorDiccionario(diccio, clave, nuevo_valor):
    diccionario = json.loads(diccio)
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return diccionario
    else:
        return False

def show_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#http://localhost:5000/dict/{"uno": "1", "dos": "2", "tres": "3"}
```
a


