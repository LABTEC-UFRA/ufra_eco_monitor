from datetime import datetime
from statistics import mean

class ClassificacaoClimatica:
    def __init__(self, temps_media = None, umidade = None, indice_uv = None, pp= None, velocidade_vento = None, data = None, rg = None ,evapo = None):
        self.erro              = ""
        self.temperatura_media = temps_media
        self.umidade           = umidade
        self.indice_uv         = indice_uv
        self.velocidade_vento  = velocidade_vento
        self.radiacao_global   = rg
        self.evapotranspiracao = evapo
        self.precipitacao      = pp
        self.data              = data
    @property
    def temperatura_media(self):
        return self.__temperatura_media
    
    @temperatura_media.setter
    def temperatura_media(self, temps_media):
        # media = mean(temps_media)        
        self.__temperatura_media = temps_media

    @property
    def umidade(self):
        return self.__umidade
    
    @umidade.setter
    def umidade(self, umidade):
        # media = mean(umidade)
        if self.__validar_umidade(umidade): 
            self.__umidade = umidade

    @property
    def indice_uv(self):
        return self.__indice_uv
    
    @indice_uv.setter
    def indice_uv(self, indice_uv):
        # media = mean(indice_uv)
        if self.__validar_indice_uv(indice_uv): 
            self.__indice_uv = indice_uv
        else:
            self.__indice_uv = -1
          
    @property
    def velocidade_vento(self):
        return self.__velocidade_vento

    @velocidade_vento.setter
    def velocidade_vento(self, velocidade_vento):
        # media = mean(velocidade_vento)
        if self.__validar_velocidade_vento(velocidade_vento):
            self.__velocidade_vento = velocidade_vento
        else:
            self.__velocidade_vento = -1 

    @property
    def radiacao_global(self):
        return self.__radiacao_global
    
    @radiacao_global.setter
    def radiacao_global(self, rg):
        if self.__validar_radiacao_global(rg):
            self.__radiacao_global = rg 
        else:
            self.__radiacao_global = -1


    @property
    def evapotranspiracao(self):
        return self.__evapotranspiracao
    
    @evapotranspiracao.setter
    def evapotranspiracao(self, evapo):
        if self.__validar_evapotranspiracao(evapo):
            self.__evapotranspiracao = evapo
        else:
            self.__evapotranspiracao= -1

    @property
    def precipitacao (self):
        return self.__precipitacao
    
    @precipitacao.setter
    def precipitacao(self,pp):
        if self.__validar_precipitacao(pp):
            self.__precipitacao = pp
        else:
            self.__validar_precipitacao = -1    


    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        if self.__validar_data(data):
            self.__data = data
        else:
            self.__validar_data = -1
        
    
    def __validar_umidade(self, umidade) -> bool:      
        valido = False
        if isinstance(umidade, (int, float)) and umidade >= 0:
            valido = True
        else:
            self.erro = "A umidade deve estar entre 0 e 100" 
        return valido

    def __validar_indice_uv(self, indice_uv) -> bool:
        valido = False
        if isinstance(indice_uv, (int, float)) and indice_uv>= 0:

            valido = True
        else:
            self.erro = "Índice UV inválido. Deve estar entre 0 e 11."
        return valido

    def __validar_velocidade_vento(self, velocidade) -> bool:
        valido = False
        if isinstance(velocidade, (int, float)) and velocidade >= 0:
            valido = True
        else:
            print("A velocidade do vento deve ser um número positivo.")
        return valido

    def __validar_radiacao_global(self, rg) -> bool:
        valido = False
        if isinstance(rg, (int, float)) and rg >= 0:

           valido = True
        else:
            print("radiação global inválida.")
        return valido


    def __validar_evapotranspiracao(self, evapo) -> bool:
        valido = False
        if isinstance(evapo, (int, float)) and evapo>= 0:

            valido = True
        else:
            print("Evapotranspiração muito alta!")
        return valido
    
    def __validar_precipitacao(self, pp) -> bool:
        valido = False
        if isinstance(pp, (int, float)) and pp >= 0:

            valido = True
        else:
            print("invalido")
        return valido    
    
    def __validar_data(self, data) -> bool: 
        valido = False
        if isinstance(data, str):
            try:
                datetime.strptime(data, "%d/%m/%Y") 
                valido = True 
            except ValueError as e:
                print(f"A data deve estar no formato DD/MM/AAAA.\n{e}")
        else:
            print("A data deve ser uma string.")
        return valido
    


    def __str__(self):        
        classificacao = f"""
         CLASSIFICAÇÃO CLIMÁTICA 
        --------------------------
        Data: {self.data}
        Temperatura Média: {self.temperatura_media:.2f}°C
        Umidade: {self.umidade}%
        Índice UV: {self.indice_uv}
        velocidade do vento: {self.velocidade_vento}
        Radiação Global : {self.radiacao_global}
        Evapotranspiração: {self.evapotranspiracao}
        Precipitação: {self.precipitacao}
        --------------------------
        """
        return classificacao
    

