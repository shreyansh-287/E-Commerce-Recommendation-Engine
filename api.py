from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

from src.data_loader import get_user_item_data
from src.similarity import build_item_similarity
from src.evaluation import train_test_split_by_time
from src.recommender import recommend_products

app = FastAPI(title="E-Commerce Recommendation Engine API")

# ---------------- LOAD MODEL ON STARTUP ----------------
print("Loading data and building model...")

df = get_user_item_data()
train_df, test_df = train_test_split_by_time(df)
similarity_df = build_item_similarity(train_df[['user_id', 'product_id', 'total_interaction_score']])

print("Model loaded successfully.")


# ---------------- REQUEST SCHEMA ----------------
class RecommendationRequest(BaseModel):
    user_ids: List[int]
    top_n: int = 5


# ---------------- RESPONSE SCHEMA (OPTIONAL BUT CLEAN) ----------------
class RecommendationResponse(BaseModel):
    results: Dict[int, List[int]]


# ---------------- HEALTH CHECK ----------------
@app.get("/")
def health_check():
    return {"status": "Recommendation API is running"}


# ---------------- POST RECOMMENDATIONS API ----------------
@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(request: RecommendationRequest):
    results = {}

    for user_id in request.user_ids:
        recs = recommend_products(user_id, train_df, similarity_df, top_n=request.top_n)

        # We return empty list if no recs instead of failing whole request
        results[user_id] = recs

    return {"results": results}
