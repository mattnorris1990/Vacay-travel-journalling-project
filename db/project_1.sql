DROP TABLE IF EXISTS city_entries;
DROP TABLE IF EXISTS country_entries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    visited BOOLEAN,
    image VARCHAR(255),
    country VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    visited BOOLEAN,
    image VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE country_entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    entry_date TIMESTAMP,
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE city_entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    entry_date TIMESTAMP,
    country_id INT NOT NULL REFERENCES cities(id)
);