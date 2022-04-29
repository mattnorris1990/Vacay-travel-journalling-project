class Country:

    def __init__(self, input_name, input_image, input_continent, input_visited = False, id = None):
        self.name = input_name
        self.visited = input_visited
        self.image = input_image
        self.continent = input_continent
        self.id = id

    def update_country_visit_status(self, country):
        if country.visited == False:
            country.visited = True
        else: 
            country.visited = False
        return country

    def check_visit_status_true(self, countries):
        countries_true = []
        for country in countries:
            if country.visited == True:
                countries_true.append(country)
        return countries_true

    def check_visit_status_false(self, countries):
        countries_false = []
        for country in countries:
            if country.visited == False:
                countries_false.append(country)
        return countries_false

    def check_continent(self, countries, continent):
        countries_list = []
        
        for country in countries:
            if country.continent == continent:
                countries_list.append(country)
        return countries_list
