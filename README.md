# 🛒 E-Commerce Recommendation Engine

A production-style, end-to-end **item–item collaborative filtering** recommendation system built with **PostgreSQL, Python, FastAPI, and Streamlit**. The project demonstrates realistic data modeling, SQL feature engineering, model evaluation, API exposure, and an interactive UI.

---

## 🚀 Overview

This project builds a personalized product recommendation engine for an e-commerce platform using weighted user interaction data (views, clicks, add-to-cart, purchases). The system:

* Stores data in **PostgreSQL**
* Performs **SQL feature engineering** to build a user–item interaction matrix
* Trains an **item–item collaborative filtering model** using cosine similarity
* Evaluates using **Precision@K and Recall@K** with a time-based split
* Exposes recommendations via a **FastAPI POST endpoint** (batch users supported)
* Provides a lightweight **Streamlit UI** for interactive testing

---

## 🧠 Problem Statement

E-commerce platforms have thousands of products, causing choice overload and low conversion. The goal is to:

> **Recommend the top-N products a user is most likely to be interested in based on historical interactions.**

---

## 🏗️ Architecture

```
PostgreSQL (users, products, interactions, orders)
        ↓
SQL Feature Engineering (weighted interactions, user–item matrix)
        ↓
Python (item–item collaborative filtering, cosine similarity)
        ↓
FastAPI (POST /recommendations)
        ↓
Streamlit UI / Client
```

---

## 📁 Project Structure

```
E-Commerce-Recommendation-Engine/
│
├── api.py                 # FastAPI application
├── main.py                # Local runner (training + evaluation)
├── ui.py                  # Streamlit UI
├── src/
│   ├── __init__.py
│   ├── db.py              # DB connection
│   ├── data_loader.py     # Load data from Postgres
│   ├── similarity.py      # Item–item similarity logic
│   ├── recommender.py     # Recommendation logic
│   └── evaluation.py      # Train/test split + metrics
└── README.md
```

---

## 🗄️ Database Schema (Simplified)

* **users**: user_id, age, gender, city, signup_date
* **products**: product_id, product_name, category, price
* **interactions**: user_id, product_id, event_type, event_time
* **orders**: order_id, user_id, order_date, total_amount

A SQL view builds the **weighted interaction matrix**:

* view → 1
* click → 2
* add_to_cart → 3
* purchase → 5

---

## 🔬 Feature Engineering (SQL)

* Convert raw events to **interaction weights**
* Aggregate into **user–item interaction matrix**
* Used as input for collaborative filtering

---

## 🤖 Model

### Item–Item Collaborative Filtering

* Each product is represented as a vector of user interaction strengths
* **Cosine similarity** is used to compute product–product similarity
* For a given user, similar products to previously interacted items are recommended

---

## 📊 Evaluation

* **Time-based train/test split** (last 30 days as test)
* Metrics:

  * **Precision@K**
  * **Recall@K**

Example output:

```
Precision@5: 0.0372
Recall@5: 0.0279
```

---

## 🌐 API

### POST /recommendations

**Endpoint:**

```
POST http://127.0.0.1:8000/recommendations
```

**Payload:**

```json
{
  "user_ids": [10, 25, 42],
  "top_n": 5
}
```

**Response:**

```json
{
  "results": {
    "10": [93, 18, 161, 46, 81],
    "25": [12, 77, 5, 101, 44],
    "42": [9, 66, 3, 55, 120]
  }
}
```

---

## 🖥️ Streamlit UI

A lightweight UI allows entering user IDs and viewing recommendations interactively.

### Run UI:

```bash
streamlit run ui.py
```

---

## ⚙️ Setup & Run

### 1. Install Dependencies

```bash
pip3 install psycopg2-binary pandas scikit-learn fastapi uvicorn streamlit requests
```

### 2. Start API

```bash
uvicorn api:app --reload
```

### 3. Start UI

```bash
streamlit run ui.py
```

---

## 💡 Key Learnings

* Designing realistic data schemas for recommender systems
* SQL-based feature engineering for user behavior modeling
* Implementing collaborative filtering from scratch
* Evaluating recommender systems with offline metrics
* Exposing ML models via REST APIs
* Building interactive demos using Streamlit

---

## 📌 Resume Highlight

> Built an end-to-end e-commerce recommendation engine using collaborative filtering, SQL-based feature engineering, FastAPI for real-time inference, and Streamlit for interactive UI, evaluated using Precision@K and Recall@K.

---

## 🔮 Future Improvements

* Add content-based filtering
* Add model retraining pipeline
* Deploy using Docker + cloud
* Add authentication & caching

---

## 👤 Author

Shreyansh Pathak
