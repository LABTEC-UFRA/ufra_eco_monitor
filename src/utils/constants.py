from flet import Colors as ft_Colors 
from enum import Enum

class Colors:
    HEADER = "#4A62AA" #["#4A62AA", "#51BCCF"]
    BACKGROUND = ft_Colors.GREY_100  
    CARD_BORDER = ft_Colors.WHITE 
    TEXT = ft_Colors.BLACK 
    TITLE = ft_Colors.BLUE_GREY_700 
    OTHER = "#BE4747FF"  # Cor para outros elementos, como o fundo dos cards
    
    GRADIENT_HEADER = ["#4A62AA", "#51BCCF"] # Gradiente para o cabeçalho
    GRADIENT_CARD = ["#4A62AA", "#51BCCF"]  # Gradiente para os cards
    GRADIENT_CARD_TEXT = ["#121010", "#FFFFFF"]  # Gradiente para o texto dos cards

class IconURL(Enum):
    TEMPERATURA = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/assets/icons/temperatura-baixa.png"
    UMIDADE = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/assets/icons/weather.png"
    INDICE_UV = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/assets/icons/raios.png"
    VENTO = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/assets/icons/wind_2531693.png"
    PRECIPITACAO = "https://raw.githubusercontent.com/LABTEC-UFRA/ufra_eco_monitor/main/assets/icons/nuvem.png"