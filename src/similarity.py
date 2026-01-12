import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_item_similarity(df):
    user_item_pivot = df.pivot_table(
        index='product_id',
        columns='user_id',
        values='total_interaction_score',
        fill_value=0
    )

    similarity_matrix = cosine_similarity(user_item_pivot)

    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=user_item_pivot.index,
        columns=user_item_pivot.index
    )

    return similarity_df
