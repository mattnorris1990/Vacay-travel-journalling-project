class Place:

    def __init__(self, input_name, input_country, input_image, input_visited = False, id = None):
        self.name = input_name
        self.country = input_country
        self.visited = input_visited
        self.image = input_image
        self.id = id

def update_place_visit_status(place):
    if place.visited == False:
        place.visited = True
    else: 
        place.visited = False
    return place