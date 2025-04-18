import flet as ft
from views.components import (
    criar_cabecalho,
    criar_secao,
    criar_caixa_valor
)
from utils.constants import colors

class HomeView:
    def __init__(self, classificacao):
        self.classificacao = classificacao
    
    def build(self) -> ft.Column:
        return ft.Column([
            self._build_header(),
            ft.Container(height=20),
            self._build_icons_row(),
            ft.Container(height=20),
            self._build_sections_row(),
            ft.Container(height=20),
            self._build_values_row(),
            self._build_date_display()
        ], scroll=ft.ScrollMode.AUTO)

    def _build_header(self) -> ft.Container:
        header = criar_cabecalho()
        header.content.controls.append(
            ft.Container(
                content=ft.Text(
                    "UNIVERSIDADE FEDERAL RURAL DA AMAZÔNIA - UFRA", 
                    size=14, 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.colors.WHITE
                ),
                padding=ft.padding.only(left=40)
            )
        )
        return header

    def _build_icons_row(self) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Image(src="img/weather.png", width=170, height=120),
                ft.Image(src="img/raios.png", width=160, height=130),
                ft.Image(src="img/temperatura-baixa.png", width=170, height=130),
                ft.Image(src="img/wind_2531693.png", width=190, height=130)
            ],
            spacing=100,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _build_sections_row(self) -> ft.Row:
        return ft.Row(
            controls=[
                criar_secao("UMIDADE"),
                criar_secao("ÍNDICE UV"),
                criar_secao("TEMPERATURA"),
                criar_secao("VELOCIDADE DO VENTO")
            ],
            spacing=25,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _build_values_row(self) -> ft.Row:
        return ft.Row(
            controls=[
                self._create_value_container(self.classificacao.umidade, "%"),
                self._create_value_container(self.classificacao.indice_uv),
                self._create_value_container(self.classificacao.temperatura_media, "°C"),
                self._create_value_container(self.classificacao.velocidade_vento, "m/s")
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _create_value_container(self, value, unit: str = "") -> ft.Container:
        return ft.Container(
            width=280 if unit == "%" else 250,
            height=310,
            bgcolor=colors.BACKGROUND,
            border_radius=10,
            padding=20,
            content=ft.Column([
                criar_caixa_valor(value, unit)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )

    def _build_date_display(self) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                self.classificacao.data,
                size=26,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE
            ),
            alignment=ft.alignment.center_right,
            padding=ft.padding.only(right=40)
        )