CREATE TABLE reco.products (
    product_id    SERIAL PRIMARY KEY,
    product_name  VARCHAR(150),
    category      VARCHAR(50),
    price         NUMERIC(10,2)
);
