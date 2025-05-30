import flet as ft

class IconRow (ft.Container):
    def __init__(self, vertical: bool = False):
        super().__init__()
        
        layout_cls = ft.Column if vertical else ft.Row
        icons_size = (50, 50) if vertical else (150, 150)  # Define o tamanho dos ícones com base na orientação
        
        layout_kwargs = {
            "controls": [
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/assets/icons/temperatura-baixa.png", width=icons_size[0], height=icons_size[1]),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/assets/icons/raios.png", width=icons_size[0], height=icons_size[1]),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/assets/icons/weather.png", width=icons_size[0], height=icons_size[1]),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/assets/icons/wind_2531693.png", width=icons_size[0], height=icons_size[1]),
                ft.Image(src="https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/refs/heads/main/assets/icons/nuvem.png", width=icons_size[0], height=icons_size[1]),
            ],
            "spacing": 20,
            "alignment": ft.MainAxisAlignment.CENTER,
        }

        if not vertical:
            layout_kwargs["vertical_alignment"] = ft.CrossAxisAlignment.CENTER
        
        self.content = layout_cls(**layout_kwargs)  # Usa o layout apropriado com os argumentos definidos

        self.padding = ft.padding.all(10) # Define o espaçamento interno do contêiner
        self.alignment = ft.alignment.center  # Centraliza o conteúdo do contêiner
        self.expand = True # Permite que o contêiner ocupe todo o espaço disponível