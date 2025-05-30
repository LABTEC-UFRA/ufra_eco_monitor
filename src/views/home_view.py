# src/views/home_view.py

import flet as ft
from components.header import Header
# from components.icon_row import IconRow
# from components.label_row import LabelRow
# from components.value_cards import ValueCards
from utils.constants import Colors 
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
            build(): Constrói o layout inicial da visão.
            update_layout(page_width: int): Atualiza o layout com base na largura da tela.
            _build_date_display(): Cria um componente de exibição de data.
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
                # self._build_date_display(),
                Header(self.classificacao, header_height),# instancia do cabeçalho da aplicação
                # IconRow(),  # Linha de ícones (comentada, mas pode ser descomentada se necessário)
                # LabelRow(),  # Linha de rótulos (comentada, mas pode ser descomentada se necessário)
                # ValueCards(self.classificacao),  # Cartões de valores (comentada, mas pode ser descomentada se necessário)
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
        # Atualiza o layout com base na largura da tela
        if page_width < 700:
            layout = ft.Column([
                ft.Text("Conteúdo temporário", size=20)  # Texto temporário para visualização
                # IconRow(vertical=True),
                # LabelRow(vertical=True),
                # ValueCards(self.classificacao, vertical=True)
            ], 
            alignment=ft.MainAxisAlignment.CENTER,)
        else:
            layout = ft.Row([
                ft.Text("Conteúdo temporário", size=20, color=Colors.TEXT )  # Texto temporário para visualização
                # IconRow(),
                # LabelRow(),
                # ValueCards(self.classificacao)
            ],
            alignment=ft.MainAxisAlignment.CENTER,)

        self.dinamic_layout_container.content = layout
        self.update()  # Atualiza a view (UserControl) - necessário para refletir as mudanças no layout
       
    # def _build_date_display(self):
    #     '''
    #     Cria um componente de exibição de data.
    #     Exibe a data referente aos dados meteorológicos.
    #     Retorna:
    #         ft.Container: Um componente de contêiner que exibe a data da classificação.
    #     '''
    #     return ft.Container(
    #         content=ft.Text(
    #             f"Data: {self.classificacao.data}",
    #             size=26,
    #             weight=ft.FontWeight.BOLD,
    #             color=Colors.TEXT
    #         ),
    #         alignment=ft.alignment.center,
    #         padding=ft.padding.symmetric(horizontal=40, vertical=10),
    #         bgcolor=Colors.BACKGROUND
    #     )
