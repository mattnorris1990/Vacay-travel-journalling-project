from db.run_sql import run_sql

from models.country_entry import Country_Entry
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
