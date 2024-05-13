
CREATE TABLE IF NOT EXISTS address (
    id SERIAL PRIMARY KEY,
    street VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20)
);


CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER,
    phone_number VARCHAR(20),
    payment_mode VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS review (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES person(id),
    stars INTEGER,
    comment TEXT
);
