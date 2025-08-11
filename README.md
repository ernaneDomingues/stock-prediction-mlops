# stock-prediction-mlops

#### Estrutura do projeto

```
stock-prediction-mlops/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_adjustment.ipynb
├── src/
│   ├── main.py
├── models/
│   ├── modelo_melhor_linearregression_petr4.joblib
│   └── scaler_petr4.joblib
├── data/
│   └── dados_petr4.parquet
├── dockerfile
├── README.md
└── requirements.txt
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