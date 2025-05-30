import flet as ft
from utils.constants import Colors
from models.classificacao import ClassificacaoClimatica

class Header(ft.Container): 
    ''' 
    Classe que representa o cabeçalho da aplicação, exibindo informações institucionais e a data atual.
    Esta classe herda de ft.Container, permitindo a criação de um componente de cabeçalho personalizado.
    Atributos:
        Nenhum atributo específico é definido nesta classe.
    Métodos:
        build(): Constrói o layout do cabeçalho com informações institucionais e data.
    '''

    def __init__(self, classificacao: ClassificacaoClimatica, header_height: float = 140):
        super().__init__()
        self.classificacao = classificacao

        self.content = ft.Column(
            controls=[
                ft.Text(
                    "UNIVERSIDADE FEDERAL RURAL DA AMAZÔNIA - UFRA",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=Colors.TEXT,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(f"Data: {self.classificacao.data}",
                        size=26,
                        color=Colors.TEXT,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        self.padding = ft.padding.symmetric(horizontal=20, vertical=10)
        self.bgcolor = Colors.HEADER
        self.expand = True  # Permite que o cabeçalho ocupe todo o espaço disponível
        self.alignment = ft.alignment.center  # Centraliza o conteúdo do cabeçalho
        self.height = header_height
