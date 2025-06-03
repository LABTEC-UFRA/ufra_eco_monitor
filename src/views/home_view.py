# src/views/home_view.py

import flet as ft
from components.header import Header
from components.info_card import InfoCard
from utils.constants import IconURL
from models.classificacao import ClassificacaoClimatica as cl

class HomeView(ft.Container):
    ''' Classe que representa a visão inicial do aplicativo, exibindo informações de classificação. 
        Esta classe herda de ft.UserControl, permitindo a criação de um componente de interface do usuário personalizado.
        A visão é composta por um cabeçalho, uma exibição de data e um layout que se adapta à largura da tela.
        A classe é responsável por construir o layout inicial e atualizar o layout com base na largura da tela.
        Atributos:
            classificacao (object): Objeto que contém informações de classificação a serem exibidas.
            dinamic_layout_container (ft.Container): Contêiner que será atualizado dinamicamente com base na largura da tela.
            content (ft.Column): Coluna que contém os componentes da visão, incluindo a exibição de data e o cabeçalho.
        Métodos:
            update_layout(page_width: int): Atualiza o layout com base na largura da tela.
        '''
    def __init__(self, classificacao: cl, header_height: float = 140):
        super().__init__()
        self.classificacao = classificacao # Recebe um objeto de classificação que contém dados climaticos a serem exibidos
        self.dinamic_layout_container = ft.Container()  # Esse container será atualizado dinamicamente com base na largura da tela
        self.header_height = header_height  # Define a altura do container com base na altura do cabeçalho
        # Constrói o layout inicial da visão
        # incluindo a exibição de data, cabeçalho e layout adaptável
        self.content = ft.Column(
            controls=[
                Header(self.classificacao, self.header_height),# instancia do cabeçalho da aplicação
                self.dinamic_layout_container
            ],
            scroll=ft.ScrollMode.AUTO
        )
    
    def update_layout(self, page_width: int):
        '''
        Atualiza dinamicamente a interface dependendo do tamanho da tela.
        Se a largura for pequena, renderiza os componentes em coluna.
        Caso contrário, organiza os componentes horizontalmente.
        Ou seja, método para atualizar o layout com base na largura da tela.
        Args:
            page_width (int): A largura atual da página, usada para determinar o layout adequado.
        '''
        vertical = page_width < 700

        cards = [
            ft.Container(
                content=InfoCard("Temperatura (°C)", str(self.classificacao.temperatura_media), IconURL.TEMPERATURA.value, vertical),
                col={"xs": 12, "sm": 6, "md": 4}
            ),
            ft.Container(
                content=InfoCard("Umidade (%)", str(self.classificacao.umidade), IconURL.UMIDADE.value, vertical),
                col={"xs": 12, "sm": 6, "md": 4}
            ),
            ft.Container(
                content=InfoCard("Índice UV", str(self.classificacao.indice_uv), IconURL.INDICE_UV.value, vertical),
                col={"xs": 12, "sm": 6, "md": 4}
            ),
            ft.Container(
                content=InfoCard("Velocidade do Vento (m/s)", str(self.classificacao.velocidade_vento), IconURL.VENTO.value, vertical),
                col={"xs": 12, "sm": 6, "md": 4}
            ),
            ft.Container(
                content=InfoCard("Precipitação (mm)", str(self.classificacao.precipitacao), IconURL.PRECIPITACAO.value, vertical),
                col={"xs": 12, "sm": 6, "md": 4}
            ),
        ]

        # layout_cls = ft.Column if vertical else ft.Row

        # self.dinamic_layout_container.content = layout_cls(
        #     controls=cards,
        #     alignment=ft.MainAxisAlignment.CENTER,
        #     spacing=20
        # )

        self.dinamic_layout_container.content = ft.ResponsiveRow(
            controls=cards,
            spacing=20,
            run_spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.update()
