import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas as pd



app = Flask(__name__)  # init

#Crea un endpoint en "/" que devuelve un html
@app.route("/", methods=['GET'])  # Default path
def default():
    fichero_html = os.path.dirname(__file__) + "\\index.html"
    print("Leyendo "+fichero_html)
    with open(fichero_html, "r") as f:
        return f.read()

dni_alba="H47584603"

#Crea un endpoint en "/trabajo_alba" que devuelve BIEN si se da el DNI correcto y MAL en caso contrario
@app.route('/trabajo_alba', methods=['GET'])
def api_all():
    token_id = None
    if 'token_id' in request.args: 
        token_id = request.args['token_id']
    
    if token_id == dni_alba:
        #return pd.read_csv('agencia_empleo_inscritos_2020.csv', sep=";").to_json(orient='records', lines=True, indent=5).replace("\n", "<br>").replace(" ", "&nbsp;")
        dump = (json
                    .dumps(
                            pd.read_csv('resources/agencia_empleo_inscritos_2020.csv', sep=";")
                                .to_dict('records'), indent=5
                            )
                            .replace("\n", "<br>")
                            .replace(" ", "&nbsp;")
                )
        
        return dump

    else:
        return "MAL"


def main():

    
    app.run(debug=True, host="0.0.0.0", port=6060)

            
if __name__ == "__main__":
    main()