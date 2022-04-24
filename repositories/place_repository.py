from db.run_sql import run_sql

from models.place import Place
from models.country import Country
import repositories.country_repository as country_repository

def save(place):
    sql = "INSERT INTO places (name, country_id, image, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [place.name, place.country.id, place.image, place.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    place.id = id
    return place

def select_all():
    places = []

    sql = "SELECT * FROM places"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        place = Place(row['name'], country, row['image'], row['visited'], row['id'])
        places.append(place)
    return places

def select(id):
    place = None
    sql = "SELECT * from places WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)

    if len(results) > 0:
        result = results[0]
        country = country_repository.select(result['country_id'])
        place = Place(result['name'], country, result['image'], result['visited'], result['id'])
        return place

def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM places WHERE id = %s"
    values = [id]
    run_sql(sql,values)

