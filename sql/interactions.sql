CREATE TABLE reco.interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id        INT REFERENCES reco.users(user_id),
    product_id     INT REFERENCES reco.products(product_id),
    event_type     VARCHAR(30),   -- view, click, add_to_cart, purchase
    event_time     TIMESTAMP
);
