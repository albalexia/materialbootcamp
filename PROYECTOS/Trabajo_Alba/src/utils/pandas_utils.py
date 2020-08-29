import pandas as pd

def leer_csv(ruta, separador=";"):
    return pd.read_csv(ruta, sep=separador)
