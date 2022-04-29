from models.country import Country

def update_country_visit_status(country):
        if country.visited == False:
            country.visited = True
        else: 
            country.visited = False
        return country

def check_visit_status_true(countries):
    countries_true = []
    for country in countries:
        if country.visited == True:
            countries_true.append(country)
    return countries_true

def check_visit_status_false(countries):
    countries_false = []
    for country in countries:
        if country.visited == False:
            countries_false.append(country)
    return countries_false

def check_continent(countries, continent):
    countries_list = []
    
    for country in countries:
        if country.continent == continent:
            countries_list.append(country)
    return countries_list

def update_place_visit_status(place):
    if place.visited == False:
        place.visited = True
    else: 
        place.visited = False
    return place
