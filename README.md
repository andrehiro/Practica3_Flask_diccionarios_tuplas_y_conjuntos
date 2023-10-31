# Practica3_Flask_diccionarios_tuplas_y_conjuntos
Andre Alexander Hidrogo Rocha 31/10/2023 Uso de parametros por medio de rutas en flask

Para lograr la implementación de esta práctica primero es necesario crear un ambiente y descargar Flask. 
Puedes usar los siguientes comandos para realizarlo:

python -m venv venv


source venv/bin/activate  # En sistemas UNIX

venv\Scripts\activate  # En sistemas Windows


pip install Flask

Para implementar el uso de diccionarios como un parametro en la ruta tenemos que hacer lo siguiente:

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

```
Utilizamos json para cargar el diccionario que obtenemos de la URL que da el usuario y después simplemente hacemos las operaciones que necesitemos con el mismo.


Para implementar el uso de conjuntos como un parámetro en la ruta tenemos que hacer lo siguiente:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/conjunto/<conjunto_param1>/<conjunto_param2>/')
def diferenciaConjuntos(conjunto_param1, conjunto_param2):
    conjunto1 = set(conjunto_param1.split(','))
    conjunto2 = set(conjunto_param2.split(','))
    
    diferenciaConjuntos = conjunto1.difference(conjunto2)

    return jsonify(list(diferenciaConjuntos))
```
Lo que cambia a comparación con los diccionarios es que ya no usamos el json, sino que lo declaramos con el set y para mostrar el conjunto debemos utilizar el jsonify.


