def recommend_products(user_id, train_df, similarity_df, top_n=5):
    user_data = train_df[train_df['user_id'] == user_id]

    if user_data.empty:
        return []

    user_products = user_data['product_id'].unique()
    scores = {}

    for product in user_products:
        if product in similarity_df:
            similar_products = similarity_df[product]

            for sim_product, score in similar_products.items():
                if sim_product not in user_products:
                    scores[sim_product] = scores.get(sim_product, 0) + score

    ranked_products = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    recommended_product_ids = [prod_id for prod_id, _ in ranked_products[:top_n]]

    return recommended_product_ids
