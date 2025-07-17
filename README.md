# stock-prediction-mlops

#### Estrutura do projeto

```
stock-prediction-mlops/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_model_serialization.ipynb
├── src/
│   ├── data/
│   ├── models/
│   ├── api/
│   └── monitoring/
├── docker/
├── tests/
├── docs/
└── deployment/
```

#### Estrutura da API

```
app/
├── main.py              # Aplicação principal
├── models/
│   ├── prediction.py    # Schemas Pydantic
│   └── response.py      # Modelos de resposta
├── services/
│   ├── predictor.py     # Lógica de predição
│   └── data_service.py  # Coleta de dados
├── utils/
│   └── preprocessing.py # Preprocessamento
└── config.py           # Configurações

```