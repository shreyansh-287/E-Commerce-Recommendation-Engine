CREATE OR REPLACE VIEW reco.weighted_interactions AS
SELECT
    user_id,
    product_id,
    CASE 
        WHEN event_type = 'view' THEN 1
        WHEN event_type = 'click' THEN 2
        WHEN event_type = 'add_to_cart' THEN 3
        WHEN event_type = 'purchase' THEN 5
        ELSE 0
    END AS interaction_weight
FROM reco.interactions;