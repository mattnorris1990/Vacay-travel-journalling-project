class Country:

    def __init__(self, input_name, input_image, input_continent, input_visited = False, id = None):
        self.name = input_name
        self.visited = input_visited
        self.image = input_image
        self.continent = input_continent
        self.id = id
