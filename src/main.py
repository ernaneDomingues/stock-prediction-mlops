import os
from fastapi import FastAPI, Query
import joblib
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

app = FastAPI(title="Stock Price Predictor")

# Caminhos relativos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "melhor_modelo_linearregression_petr4.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler_petr4.joblib")

# Carrega modelo e scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def get_features_from_ticker(ticker: str):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    df = yf.download(ticker, start=start_date, end=end_date)
    df = df[['Close']]
    
    # Criar features
    df['Close_lag1'] = df['Close'].shift(1)
    df['Close_lag2'] = df['Close'].shift(2)
    df['Close_lag3'] = df['Close'].shift(3)
    df['ma_5'] = df['Close'].rolling(window=5).mean()
    df['ma_10'] = df['Close'].rolling(window=10).mean()
    df.dropna(inplace=True)

    latest_features = df.iloc[-1][['Close_lag1','Close_lag2','Close_lag3','ma_5','ma_10']].values.reshape(1, -1)
    latest_scaled = scaler.transform(latest_features)
    return latest_scaled

@app.get("/")
def home():
    return {"status": "API online", "message": "Use /predict-price?ticker=PETR4.SA para prever o preço"}

@app.get("/health")
def home():
    return {"status": "API online"}

@app.get("/predict-price")
def predict_price(ticker: str = Query(..., description="Ticker da empresa, ex: PETR4.SA")):
    try:
        features = get_features_from_ticker(ticker)
        prediction = model.predict(features)[0]
        return {
            "ticker": ticker,
            "predicted_price": round(float(prediction), 2),
            "prediction_date": datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        return {"error": str(e)}
