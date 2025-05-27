import flet as ft
import pandas as pd
from datetime import datetime
import os

# Classes originais adaptadas para Flet
class ClassificacaoClimatica:
    def __init__(self, temps_media=None, umidade=None, indice_uv=None, pp=None, 
                 velocidade_vento=None, data=None, rg=None, evapo=None):
        self.temperatura_media = temps_media
        self.umidade = umidade
        self.indice_uv = indice_uv
        self.velocidade_vento = velocidade_vento
        self.radiacao_global = rg
        self.evapotranspiracao = evapo
        self.precipitacao = pp
        self.data = data

class Leitor:
    def leitor_pandas(self, dir_arquivo: str):
        print(f"Diretorio atual: {os.path.abspath(dir_arquivo)}")
        return pd.read_csv(dir_arquivo, encoding="utf-8", sep=';')

# Aplicação principal Flet
def main(page: ft.Page):
    # Configuração da página
    page.title = "ECOMONITOR"
    page.window.width = 1341
    page.window.height = 749  
    page.bgcolor = ft.Colors("white")
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    # Carrega os dados
    leitor = Leitor()
    df = leitor.leitor_pandas(r'.\files\BD_diario.csv')
    
    classificacao = ClassificacaoClimatica(
        temps_media=df['Tmed'].iloc[-1],
        umidade=df['UR'].iloc[-1],
        indice_uv=df['Indice UV'].iloc[-1],
        velocidade_vento=df['U2'].iloc[-1],
        evapo=df['ET (mm/dia)'].iloc[-1],
        rg=df['Rg (MJ)'].iloc[-1],
        pp=df['PP'].iloc[-1],
        data=df['Data'].iloc[-1]
    )

    # Componentes da interface
    def criar_secao(title, bg_color=ft.colors.BLUE_GREY_100):
        return ft.Container(
            width=300,
            height=150,
            bgcolor=bg_color,
            border_radius=10,
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Column([
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                # ft.Text(f"{value}{unit}", size=30, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    def definir_valores_caixa(value, unit="", bg_color=ft.colors.BLUE_GREY_600):
        return ft.Container(
            width=300,
            height=150,
            bgcolor=bg_color,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(f"{value}{unit}", size=48, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE,  text_align=ft.TextAlign.CENTER)
        )

    # Cabeçalho
    header = ft.Container(
    width=1440,
    height=240,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors=["#4A62AA", "#51BCCF"]
    ),
    content=ft.Column([
        ft.Container(
            content=ft.Text("ECOMONITOR", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            padding=ft.padding.only(left=40, top=20),
        ),
        ft.Container(
            content=ft.Text("UNIVERSIDADE FEDERAL RURAL DA AMAZÔNIA - UFRA", size=14, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            padding=ft.padding.only(left=40, top=5),
        ),
        ft.Container(
            content=ft.Text(classificacao.data, size=26, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            padding=ft.padding.only(left=40, top=10),
        )
    ])
)

    # Ícones
    icons_row = ft.Row(
        controls=[
            ft.Image(src="img/weather.png", width=170, height=120, fit=ft.ImageFit.CONTAIN),
            ft.Image(src="img/raios.png", width=160, height=130, fit=ft.ImageFit.CONTAIN),
            ft.Image(src="img/temperatura-baixa.png", width=170, height=130, fit=ft.ImageFit.CONTAIN),
            ft.Image(src="img/wind_2531693.png", width=190, height=130, fit=ft.ImageFit.CONTAIN)
        ],
        spacing=100,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Seções de métricas
    sections_row = ft.Row(
        controls=[
            criar_secao("UMIDADE", ft.colors.BLUE_GREY_400),
            criar_secao("ÍNDICE UV", ft.colors.BLUE_GREY_400),
            criar_secao("TEMPERATURA", ft.colors.BLUE_GREY_400),
            criar_secao("VELOCIDADE DO VENTO", ft.colors.BLUE_GREY_400)
        ],
        spacing=25,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Valores numéricos
    values_row = ft.Row(
        controls=[
            ft.Container(
                width=280,
                height=310,
                bgcolor="#EEF4DD",
                border_radius=10,
                padding=20,
                content=ft.Column([
                    definir_valores_caixa(classificacao.umidade, "%")
                ], alignment=ft.MainAxisAlignment.CENTER)
            ),
            ft.Container(
                width=250,
                height=310,
                bgcolor="#EEF4DD",
                border_radius=10,
                padding=20,
                content=ft.Column([
                    definir_valores_caixa(classificacao.indice_uv, "")
                ], alignment=ft.MainAxisAlignment.CENTER)
            ),
            ft.Container(
                width=280,
                height=310,
                bgcolor="#EEF4DD",
                border_radius=10,
                padding=20,
                content=ft.Column([
                    definir_valores_caixa(classificacao.temperatura_media, "°C")
                ], alignment=ft.MainAxisAlignment.CENTER)
            ),
            ft.Container(
                width=260,
                height=310,
                bgcolor="#EEF4DD",
                border_radius=10,
                padding=20,
                content=ft.Column([
                    definir_valores_caixa(classificacao.velocidade_vento, "m/s")
                ], alignment=ft.MainAxisAlignment.CENTER)
            )
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Data
    date_display = ft.Container(
        content=ft.Text(
            classificacao.data,
            size=26,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE
        ),
        alignment=ft.alignment.center_right,
        padding=ft.padding.only(right=40)
    )

    # Layout principal
    page.add(
        ft.Column([
            header, ft.Container(height=20),
            icons_row, ft.Container(height=20),
            sections_row, ft.Container(height=20),
            values_row, 
            date_display
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)