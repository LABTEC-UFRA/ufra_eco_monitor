import os
print("Diretório atual:", os.getcwd())

import flet as ft
from models.leitor import Leitor
from models.classificacao import ClassificacaoClimatica
from views.home_view import HomeView


# Elementos da interface
# titulo = ft.Text("Bem-vindo ao ECOMONITOR", size=24, weight="bold")
#botao = ft.ElevatedButton("Atualizar Dados")


def main(page: ft.Page):
    # Configuração da página
    page.title = "ECOMONITOR"
    # page.window.width = 1341
    # page.window.height = 749  
    page.bgcolor = ft.colors.WHITE
    page.padding = 0

    # Carrega os dados
    leitor = Leitor()
    # df = leitor.leitor_pandas(r'files\BD_diario.csv')
    csv_url = 'https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/files/BD_diario.csv'
    df = leitor.leitor_pandas(csv_url)
    
    classificacao = ClassificacaoClimatica(
       
        data=df['Data'].iloc[-1],
        temps_media=df['Tmed'].iloc[-1],
        umidade=df['UR'].iloc[-1],
        indice_uv=df['Indice UV'].iloc[-1],
        velocidade_vento=df['U2'].iloc[-1],
        rg=df['Rg (MJ)'].iloc[-1],
        evapo=df['ET (mm/dia)'].iloc[-1],
        pp=df['PP'].iloc[-1]
    )

    # Cria e adiciona a view principal
    home_view = HomeView(classificacao)
    # page.add(home_view.build())
    view_column = home_view.build()

    # Define eventos de redimensionamento
    def atualizar_layout(e):
        largura = page.width
        view_column.controls[2].content = home_view._layout_por_largura(largura) # type: ignore
        page.update()
    
    #Atualiza o layout ao redimensionar a janela
    page.on_resize = atualizar_layout # type: ignore

    # Primeira renderização
    view_column.controls[2].content = home_view._layout_por_largura(page.width) # type: ignore
    # page.on_view_pop = lambda e: view_column.controls[2].content = home_view._layout_por_largura(page.width)  # Essa linha garante que o layout seja atualizado ao voltar para a view
    page.add(view_column)

ft.app(target=main,  view=ft.WEB_BROWSER) # type: ignore