import pandas as pd

def train_test_split_by_time(df, test_days=30):
    df['event_time'] = pd.to_datetime(df['event_time'])
    cutoff = df['event_time'].max() - pd.Timedelta(days=test_days)

    train_df = df[df['event_time'] <= cutoff]
    test_df = df[df['event_time'] > cutoff]

    return train_df, test_df


def precision_recall_at_k(train_df, test_df, similarity_df, k=5):
    users = test_df['user_id'].unique()
    precisions = []
    recalls = []

    for user in users:
        test_items = test_df[test_df['user_id'] == user]['product_id'].unique()
        train_items = train_df[train_df['user_id'] == user]['product_id'].unique()

        if len(train_items) == 0:
            continue

        scores = {}

        for item in train_items:
            if item in similarity_df:
                similar_items = similarity_df[item]
                for sim_item, score in similar_items.items():
                    if sim_item not in train_items:
                        scores[sim_item] = scores.get(sim_item, 0) + score

        ranked_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        recommended_items = [item for item, _ in ranked_items[:k]]

        if len(recommended_items) == 0:
            continue

        hits = len(set(recommended_items) & set(test_items))
        precision = hits / k
        recall = hits / len(test_items) if len(test_items) > 0 else 0

        precisions.append(precision)
        recalls.append(recall)

    if len(precisions) == 0:
        return 0, 0

    return sum(precisions) / len(precisions), sum(recalls) / len(recalls)
