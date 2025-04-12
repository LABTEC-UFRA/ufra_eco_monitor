import pandas as pd
import os

class Leitor:
    def leitor_pandas(self, dir_arquivo: str):
        print(f"Diretorio atual: {os.path.abspath(dir_arquivo)}")
        return pd.read_csv(dir_arquivo, encoding="utf-8", sep=';')