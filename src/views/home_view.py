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
        # Contêiner dinâmico onde o layout vai mudar baseado na largura da tela
        self.layout_container = ft.Container()

        def atualizar_layout(e):
            largura = e.page.width
            self.layout_container.content = self._layout_por_largura(largura)
            e.page.update()

        def on_page_load(e):
            self.layout_container.content = self._layout_por_largura(e.page.width)

        # Evento para redimensionamento da tela
        ft.Page.on_resized = atualizar_layout  
        ft.Page.on_view_pop = on_page_load 

        return ft.Column([
            self._build_date_display(),
            self._build_header(),
            self.layout_container
        ], scroll=ft.ScrollMode.AUTO)

    def _layout_por_largura(self, largura):
        # Define se os elementos devem ser organizados em linha ou coluna
        if largura < 700:
            return ft.Column([
                self._build_icons_row(vertical=True),
                self._build_sections_row(vertical=True),
                self._build_values_row(vertical=True)
            ], alignment=ft.MainAxisAlignment.CENTER)
        else:
            return ft.Column([
                self._build_icons_row(),
                self._build_sections_row(),
                self._build_values_row()
            ])

    def _build_header(self) -> ft.Container:
        header = criar_cabecalho()
        header.content.controls.append(  # type: ignore
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

    def _build_icons_row(self, vertical=False):
        layout = ft.Column if vertical else ft.Row
        return layout(
            controls=[
                ft.Image(src="img/humidity.png", width=120, height=90),
                ft.Image(src="img/raios.png", width=120, height=90),
                ft.Image(src="img/temperatura-baixa.png", width=120, height=90),
                ft.Image(src="img/wind_2531693.png", width=120, height=90),
                ft.Image(src="img/wind_2531693.png", width=120, height=90)
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _build_sections_row(self, vertical=False):
        layout = ft.Column if vertical else ft.Row
        return layout(
            controls=[
                criar_secao("UMIDADE"),
                criar_secao("ÍNDICE UV"),
                criar_secao("TEMPERATURA"),
                criar_secao("VELOCIDADE DO VENTO"),
                criar_secao("Precipitação")
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _build_values_row(self, vertical=False):
        layout = ft.Column if vertical else ft.Row
        return layout(
            controls=[
                self._create_value_container(self.classificacao.umidade, "%"),
                self._create_value_container(self.classificacao.indice_uv),
                self._create_value_container(self.classificacao.temperatura_media, "°C"),
                self._create_value_container(self.classificacao.velocidade_vento, "m/s"),
                self._create_value_container(self.classificacao.precipitacao, "mm")
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def _create_value_container(self, value, unit: str = "") -> ft.Container:
        # return ft.Container(
        #     width=280 if unit == "%" else 250,
        #     # Lembrar de comentar a linha abaixo
        #     border=ft.border.all(1, ft.colors.WHITE),#trecho apenas para testes visuais
        #     height=110,
        #     bgcolor=colors.BACKGROUND,
        #     border_radius=10,
        #     padding=20,
        #     content=ft.Column([
        #         criar_caixa_valor(value, unit)
        #     ], alignment=ft.MainAxisAlignment.CENTER)
        # )
        return ft.Container(
            width=200,
            # Lembrar de comentar a linha abaixo
            border=ft.border.all(1, ft.colors.WHITE),# trecho apenas para testes visuais
            height=100,
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
            f"Data: {self.classificacao.data}",  
            size=26,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLACK
        ),
        alignment=ft.alignment.center,  
        padding=ft.padding.symmetric(horizontal=40, vertical=10),  
        bgcolor=ft.colors.GREY_200  
    )
        