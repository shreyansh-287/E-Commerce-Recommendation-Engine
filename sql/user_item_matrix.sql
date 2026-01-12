CREATE OR REPLACE VIEW reco.user_item_matrix AS
SELECT
    user_id,
    product_id,
    SUM(interaction_weight) AS total_interaction_score
FROM reco.weighted_interactions
GROUP BY user_id, product_id;
