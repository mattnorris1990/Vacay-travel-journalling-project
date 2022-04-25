DROP TABLE IF EXISTS place_entries;
DROP TABLE IF EXISTS country_entries;
DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    visited BOOLEAN,
    image VARCHAR(255)
);

CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    visited BOOLEAN,
    image VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE country_entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    text_entry TEXT,
    image VARCHAR(255),
    date_stamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE place_entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    entry_date TIMESTAMP,
    place_id INT NOT NULL REFERENCES places(id)
);