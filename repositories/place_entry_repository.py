from db.run_sql import run_sql

from models.place_entry import Place_Entry
from models.place import Place
import repositories.place_repository as place_repository

def save(place_entry):
    sql = "INSERT INTO place_entries (title, text_entry, image, place_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [place_entry.title, place_entry.text, place_entry.image, place_entry.place.id]
    results = run_sql(sql,values)
    
    id = results[0]['id']
    place_entry.id = id
    
    date_stamp = results[0]['date_stamp']
    place_entry.date_stamp = date_stamp

    return place_entry

def select_all():
    entries = []

    sql = "SELECT * FROM place_entries ORDER BY (id)"
    results = run_sql(sql)

    for row in results:
        place = place_repository.select(row['place_id'])
        entry = Place_Entry(row['title'], row['text_entry'], row['image'], place, row['date_stamp'], row['id'])
        entries.append(entry)
    return entries

def select(id):
    entry = None
    sql = "SELECT * from place_entries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        place = place_repository.select(result['place_id'])
        entry = Place_Entry(result['title'], result['text_entry'], result['image'], place, result['date_stamp'], result['id'])
        return entry

def delete_all():
    sql = "DELETE FROM place_entries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM place_entries WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(place_entry):
    sql = "UPDATE place_entries SET (title, text_entry, image, country_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [place_entry.title, place_entry.text, place_entry.image, place_entry.country.id, place_entry.id]
    run_sql(sql, values)

