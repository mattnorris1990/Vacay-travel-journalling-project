from db.run_sql import run_sql

from models.country import Country
from models.place import Place

def save(country):
    sql = "INSERT INTO countries (name, visited, image) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.visited, country.image]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries ORDER BY (name)"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['image'], row['visited'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None

    sql = "SELECT * from countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        country = Country(result['name'], result['image'], result['visited'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, visited, image) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.image, country.id]
    run_sql(sql, values)

def list_places(country):
    places = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        place  = Place(row['name'], row['country_id'], row['image'], row['visited'], row)
        places.append(place)
    return places