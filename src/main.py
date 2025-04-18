import flet as ft
from models.leitor import Leitor
from models.classificacao import ClassificacaoClimatica
from views.home_view import HomeView

def main(page: ft.Page):
    # Configuração da página
    page.title = "ECOMONITOR"
    page.window.width = 1341
    page.window.height = 749  
    page.bgcolor = ft.colors.WHITE
    page.padding = 0

    # Carrega os dados
    leitor = Leitor()
    df = leitor.leitor_pandas(r'.\files\BD_diario.csv')
    
    classificacao = ClassificacaoClimatica(
        temps_media=df['Tmed'].iloc[-1],
        umidade=df['UR'].iloc[-1],
        indice_uv=df['Indice UV'].iloc[-1],
        velocidade_vento=df['U2'].iloc[-1],
        data=df['Data'].iloc[-1]
    )

    # Cria e adiciona a view principal
    home_view = HomeView(classificacao)
    page.add(home_view.build())

ft.app(target=main)