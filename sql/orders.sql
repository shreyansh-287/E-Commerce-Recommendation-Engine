CREATE TABLE reco.orders (
    order_id     SERIAL PRIMARY KEY,
    user_id      INT REFERENCES reco.users(user_id),
    order_date   DATE,
    total_amount NUMERIC(10,2)
);
