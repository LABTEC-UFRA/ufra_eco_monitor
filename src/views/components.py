import flet as ft
from utils.constants import colors

def criar_secao(title: str, bg_color: str = colors.SECTION_BG) -> ft.Container:
    return ft.Container(
        width=300,
        height=150,
        bgcolor=bg_color,
        border_radius=10,
        padding=10,
        alignment=ft.alignment.center,
        content=ft.Column([
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
        ], alignment=ft.MainAxisAlignment.CENTER, 
           horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

def criar_caixa_valor(value, unit: str = "", bg_color: str = colors.VALUE_BOX) -> ft.Container:
    return ft.Container(
        width=300,
        height=150,
        # Lembrar de comentar a linha abaixo
        border=ft.border.all(1, ft.colors.BLACK),#trecho apenas para testes visuais
        bgcolor=bg_color,
        border_radius=10,
        alignment=ft.alignment.center,
        content=ft.Text(f"{value}{unit}", 
                       size = 38,
                       weight = ft.FontWeight.BOLD, 
                       color = ft.colors.WHITE)
    )

def criar_cabecalho() -> ft.Container:
    return ft.Container(
        width=1440,
        height=240,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=colors.HEADER_GRADIENT
        ),
        content=ft.Column([
            ft.Container(
                content=ft.Text("ECOMONITOR", 
                              size=36, 
                              weight=ft.FontWeight.BOLD, 
                              color=ft.colors.WHITE),
                padding=ft.padding.only(left=40, top=20)
            ),
        ])
    )
