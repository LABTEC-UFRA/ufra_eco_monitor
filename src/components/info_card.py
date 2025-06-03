# src/components/info_card.py

import flet as ft
from utils.constants import Colors

class InfoCard(ft.Container):
    """
    Um cartão de informação que exibe um ícone, título e valor.
    Pode ser orientado vertical ou horizontalmente.
    """

    def __init__(self, titulo: str, valor: str, icon_url: str, vertical: bool = False, width: int = 200, height: int = 140):
        super().__init__()

        icon = ft.Image(src=icon_url, width=50, height=50)
        titulo_text = ft.Text(titulo, size=14, weight=ft.FontWeight.BOLD, color=Colors.TEXT)
        valor_text = ft.Text(valor, size=18, weight=ft.FontWeight.BOLD, color=Colors.TITLE)

        layout = ft.Column([
            icon,
            titulo_text,
            valor_text
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER) if vertical else ft.Row([
            icon,
            ft.Column([
                titulo_text,
                valor_text
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.content = layout
        self.padding = 10
        self.border_radius = 10
        self.border = ft.border.all(1, Colors.CARD_BORDER)
        self.bgcolor = Colors.BACKGROUND
        self.width = width
        self.height = height
