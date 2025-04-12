from datetime import datetime
from statistics import mean

class ClassificacaoClimatica:
    def __init__(self, temps_media=None, umidade=None, indice_uv=None, pp=None, 
                 velocidade_vento=None, data=None, rg=None, evapo=None):
        self.temperatura_media = temps_media
        self.umidade = umidade
        self.indice_uv = indice_uv
        self.velocidade_vento = velocidade_vento
        self.radiacao_global = rg
        self.evapotranspiracao = evapo
        self.precipitacao = pp
        self.data = data

    # TODO: falta colocar os getters/setters e métodos de validação originais