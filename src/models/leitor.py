import pandas as pd

class Leitor:
    # def leitor_pandas(self, dir_arquivo: str):
    #     return pd.read_csv(dir_arquivo, encoding="utf-8", sep=';')

    def __init__(self, caminho_csv: str):
        self.caminho_csv = caminho_csv

    def __leitor_pandas(self) -> pd.DataFrame:
        return pd.read_csv(self.caminho_csv, encoding="utf-8", sep=';')

    def ultimo_registro(self) -> pd.Series:
        df = self.__leitor_pandas()
        return df.iloc[-1]