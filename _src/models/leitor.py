import pandas as pd
import os

class Leitor:
    def leitor_pandas(self, dir_arquivo: str):
        return pd.read_csv(dir_arquivo, encoding="utf-8", sep=';')