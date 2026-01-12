from src.data_loader import get_user_item_data
from src.similarity import build_item_similarity
from src.evaluation import train_test_split_by_time, precision_recall_at_k
from src.recommender import recommend_products

def main():
    print("Fetching data from Postgres...")
    df = get_user_item_data()

    print("Splitting into train and test...")
    train_df, test_df = train_test_split_by_time(df)

    print("Building item-item similarity matrix...")
    similarity_df = build_item_similarity(train_df[['user_id', 'product_id', 'total_interaction_score']])

    print("Evaluating model...")
    precision, recall = precision_recall_at_k(train_df, test_df, similarity_df, k=5)

    print(f"\nPrecision@5: {precision:.4f}")
    print(f"Recall@5: {recall:.4f}")

    test_user_id = 10
    print(f"\nTop recommendations for user {test_user_id}:")
    recommendations = recommend_products(test_user_id, train_df, similarity_df, top_n=5)
    print(recommendations)


if __name__ == "__main__":
    main()
