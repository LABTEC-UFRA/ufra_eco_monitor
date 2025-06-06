import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src")) # Adiciona o diretório src ao caminho do sistema para importações

import flet as ft
import pandas as pd
from models.leitor import Leitor
from models.classificacao import ClassificacaoClimatica
from views.home_view import HomeView
from utils.constants import Colors  # Importa a cor definida no arquivo constants.py
from typing import Optional

class EcoMonitorApp:
    def __init__(self):
        self.home_view: Optional[HomeView] = None

    def carregar_dados(self) -> ClassificacaoClimatica:
        url_csv = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/files/BD_diario.csv"
        leitor = Leitor(url_csv)
        ultimo = leitor.ultimo_registro()

        return ClassificacaoClimatica(
            data_ = ultimo['Data'],
            temps_media = ultimo['Tmed'],
            umidade_ = ultimo['UR'],
            ind_uv = ultimo['Indice UV'],
            velo_vento = ultimo['U2'],
            rad_global = ultimo['Rg (MJ)'],
            evapotranspiracao_ = ultimo['ET (mm/dia)'],
            precip = ultimo['PP']
        )

    def main(self, page: ft.Page):
        page.title = "ECOMONITOR - UFRA"
        page.bgcolor = Colors.BACKGROUND if hasattr(Colors, 'BACKGROUND') else Colors.OTHER
        page.padding = 0
        page.scroll = ft.ScrollMode.AUTO  # Permite rolagem automática se o conteúdo exceder a altura da página
        
        page.update()
        header_height: float = page.height * 0.2  # 20% da altura da tela # type: ignore
        #print(f"Altura da página: {page.height}, Header Height: {header_height}")  # type: ignore

        classificacao = self.carregar_dados()
        self.home_view = HomeView(classificacao, header_height=header_height)
        page.add(self.home_view)
        #self.home_view.update_layout(page.width) # type: ignore


        def on_resize(e: ft.ControlEvent):
            ''' Função para atualizar o layout quando a janela é redimensionada.
                Atualiza o layout da home_view com base na nova largura da página.
            '''
            if self.home_view:
                if self.home_view:
                    # Verifica se a home_view já foi inicializada
                    self.home_view.update_layout(e.page.width)
            self.home_view.update_layout(e.page.width) # type: ignore

        page.on_resize = on_resize # Atualiza o layout quando a janela é redimensionada # type: ignore
        self.home_view.update_layout(page.width) # type: ignore


if __name__ == "__main__":
    app = EcoMonitorApp()
    ft.app(target=app.main)
