import flet as ft

class IconRow (ft.Container):
    def __init__(self, vertical: bool = False):
        super().__init__()
        
        layout = ft.Column if vertical else ft.Row

        self.content = layout(
            controls=[
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/images/ico_temp.png"),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/images/ico_umidade.png"),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/images/ico_uv.png"),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/images/ico_vento.png"),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/images/ico_rad_global.png"),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER if not vertical else None # type: ignore            
        )
        self.padding = ft.padding.all(10) # Define o espaçamento interno do contêiner
        self.alignment = ft.alignment.center  # Centraliza o conteúdo do contêiner
        self.expand = True # Permite que o contêiner ocupe todo o espaço disponível