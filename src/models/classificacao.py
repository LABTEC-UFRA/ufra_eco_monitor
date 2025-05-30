from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class ClassificacaoClimatica:
    temps_media: float
    umidade_: float
    ind_uv: float
    velo_vento: float
    rad_global: float
    evapotranspiracao_: float
    precip: float # Precipitação
    data_: str
    erro: str = field(init=False, default="")  # campo que não será passado no construtor

    def __post_init__(self):
        ''' 
        Método chamado após a inicialização do dataclass para validar os dados. 
        Ele verifica se os valores fornecidos atendem aos critérios esperados.
        '''

        if not isinstance(self.temps_media, (int, float)):
            raise TypeError("A temperatura média deve ser um número.")
        
        if not self.__validar_umidade(self.umidade_):
            raise ValueError(self.erro)
        
        if not self.__validar_indice_uv(self.ind_uv):
            raise ValueError(self.erro)
        
        if not self.__validar_velocidade_vento(self.velo_vento):
            raise ValueError(self.erro)
        
        if not self.__validar_radiacao_global(self.rad_global):
            raise ValueError(self.erro)
        
        if not self.__validar_evapotranspiracao(self.evapotranspiracao_):
            raise ValueError(self.erro)
        
        if not self.__validar_precipitacao(self.precip):
            raise ValueError(self.erro)
        
        if not self.__validar_data(self.data_):
            raise ValueError(self.erro)
    

    @property
    def temperatura_media(self) -> float:
        return self.temps_media
    
    @property
    def umidade(self) -> float:
        return self.umidade_
    
    @property
    def indice_uv(self) -> float:
        return self.ind_uv

    @property
    def velocidade_vento(self) -> float:
        return self.velo_vento

    @property
    def radiacao_global(self) -> float:
        return self.rad_global
    
    @property
    def evapotranspiracao(self) -> float:
        return self.evapotranspiracao_

    @property
    def precipitacao(self) -> float:
        return self.precip
    
    @property
    def data(self) -> str:
        return self.data_
        
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
        Umidade: {self.umidade_}%
        Índice UV: {self.indice_uv}
        velocidade do vento: {self.velocidade_vento}
        Radiação Global : {self.radiacao_global}
        Evapotranspiração: {self.evapotranspiracao}
        Precipitação: {self.precipitacao}
        --------------------------
        """
        return classificacao
    

