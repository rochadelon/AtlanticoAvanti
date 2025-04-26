# Estrutura do Projeto

```
├── LICENSE
├── README.md               # Documentação principal do projeto
├── data
│   ├── external/           # Dados de fontes externas
│   ├── interim/            # Dados intermediários processados
│   ├── processed/          # Dados finais prontos para modelagem
│   └── raw/                # Dados originais, imutáveis
├── docs/                   # Documentação do projeto
├── models/                 # Modelos treinados e serializados
├── notebooks/              # Jupyter notebooks para exploração e comunicação
├── references/             # Artigos, manuais e materiais de referência
├── reports/                # Relatórios gerados (HTML, PDF, LaTeX)
│   └── figures/            # Gráficos e figuras geradas
├── requirements.txt        # Dependências do projeto
├── setup.py                # Script de instalação do projeto
└── src/                    # Código fonte
    ├── __init__.py
    ├── data/               # Scripts para download e processamento de dados
    ├── features/           # Scripts para transformação de features
    ├── models/             # Scripts para treinamento e avaliação de modelos
    ├── utils/              # Funções utilitárias
    └── visualization/      # Scripts para visualização
```
