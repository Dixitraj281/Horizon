from fastapi import APIRouter

router = APIRouter()

@router.get("/predict")
def predict(symbol: str):
    return {"symbol": symbol, "score": 75.5, "trend": "Bullish"}
