from db.run_sql import run_sql

from models.country_entry import CountryEntry
from models.country import Country
import repositories.country_repository as country_repository

def save(country_entry):
    sql = "INSERT INTO country_entries (title, text_entry, image, country_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country_entry.title, country_entry.text, country_entry.image, country_entry.country.id]
    results = run_sql(sql,values)
    
    id = results[0]['id']
    country_entry.id = id
    
    date_stamp = results[0]['date_stamp']
    country_entry.date_stamp = date_stamp

    return country_entry

def select_all():
    entries = []

    sql = "SELECT * FROM country_entries ORDER BY (id)"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        entry = CountryEntry(row['title'], row['text_entry'], row['image'], country, row['date_stamp'], row['id'])
        entries.append(entry)
    return entries

def select(id):
    entry = None
    sql = "SELECT * from country_entries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        country = country_repository.select(result['country_id'])
        entry = CountryEntry(result['title'], result['text_entry'], result['image'], country, result['date_stamp'], result['id'])
        return entry


def delete_all():
    sql = "DELETE FROM country_entries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM country_entries WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(country_entry):
    sql = "UPDATE country_entries SET (title, text_entry, image, country_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [country_entry.title, country_entry.text, country_entry.image, country_entry.country.id, country_entry.id]
    run_sql(sql, values)


