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

