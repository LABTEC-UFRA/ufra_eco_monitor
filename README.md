# Estação Meteorológica Local – Visualização de Dados Ambientais

Este projeto tem como objetivo desenvolver uma aplicação para visualização dos dados ambientais coletados por uma estação meteorológica local. A região onde a estação está instalada carece de plataformas acessíveis para consulta pública dos dados climáticos, que são essenciais para atividades como agricultura, planejamento urbano, estudos ambientais e prevenção de eventos extremos.

Dada a natureza offline da estação, os dados exibidos pela aplicação são referentes ao dia anterior, extraídos automaticamente de arquivos .csv gerados diariamente.

## Funcionalidades atuais

A aplicação exibe, por enquanto, os seguintes indicadores:

Velocidade do vento

Umidade do ar

Índice UV

Temperatura média diária


## Tecnologias utilizadas

Python 3.10+

Flet – criação da interface gráfica

Pandas – leitura e manipulação dos dados meteorológicos (.csv)


## Estrutura do Projeto

A organização do código busca manter uma separação clara entre as responsabilidades de leitura, visualização, lógica e dados:

.
├── Files/                  # Diretório contendo os arquivos .csv com dados meteorológicos
├── Img/                    # Imagens utilizadas na interface da aplicação
├── Src/                    # Código-fonte principal da aplicação
│   ├── models/             # Camada de dados e lógica de leitura/classificação
│   │   ├── classificacao.py    # Possivelmente classifica os dados (ex: UV alto/baixo, níveis de umidade)
│   │   └── leitor.py           # Responsável por carregar e tratar os dados dos arquivos CSV
│   ├── utils/              # Utilitários e constantes globais
│   │   └── constants.py        # Armazena valores fixos usados em diversas partes do sistema (ex: limites UV)
│   ├── views/              # Interface com o usuário (componentes visuais)
│   │   ├── compoments.py       # Componentes reutilizáveis da interface (ex: cards, gráficos, textos)
│   │   └── home_view.py        # Tela principal exibida ao iniciar a aplicação
├── main.py                 # Ponto de entrada da aplicação

## Como executar

1. Clone o repositório:

git clone https://github.com/SEU_USUARIO/NOME_DO_PROJETO.git


2. Instale as dependências:

pip install -r requirements.txt


3. Coloque os arquivos .csv no diretório Files/.


4. Execute a aplicação:

python main.py



# Próximos passos

Histórico de dados com seleção de datas
