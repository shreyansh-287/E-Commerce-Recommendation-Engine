CREATE TABLE reco.users (
    user_id      SERIAL PRIMARY KEY,
    age          INT,
    gender       VARCHAR(10),
    city         VARCHAR(50),
    signup_date  DATE
);
