import pandas as pd
from .db import get_connection

def get_user_item_data():
    conn = get_connection()
    query = """
        SELECT i.user_id, i.product_id, w.total_interaction_score, i.event_time
        FROM reco.interactions i
        JOIN reco.user_item_matrix w
          ON i.user_id = w.user_id AND i.product_id = w.product_id;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
