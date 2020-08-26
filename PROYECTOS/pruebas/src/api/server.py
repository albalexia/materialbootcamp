import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas as pd

html = """<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>TITULO</title>
</head>
<body>
HOLA MUNDO
</body>
</html>"""


app = Flask(__name__)  # init

#Crea un endpoint en "/" que devuelve un html
@app.route("/", methods=['GET'])  # Default path
def default():
    return html

#Crea un endpoint en "/trabajo_alba" que devuelve BIEN si se da el DNI correcto y MAL en caso contrario
@app.route('/trabajo_alba', methods=['GET'])
def api_all():
    token_id = None
    if 'token_id' in request.args:
        token_id = request.args['token_id']
    
    if token_id == "50000000A":
        #return pd.read_csv('agencia_empleo_inscritos_2020.csv', sep=";").to_json(orient='records', lines=True, indent=5).replace("\n", "<br>").replace(" ", "&nbsp;")
        dump = json.dumps(pd.read_csv('agencia_empleo_inscritos_2020.csv', sep=";").to_dict('records'), indent=5).replace("\n", "<br>").replace(" ", "&nbsp;")
        
        return dump

    else:
        return "MAL"


def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "\\settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()