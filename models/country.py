class Country:

    def __init__(self, input_name, input_visited = "False", id = None):
        self.name = input_name
        self.visited = input_visited
        self.image = "/images/placeholder_country_image.jpg"
        self.id = id
        

    def mark_visited(self):
        if self.visited == False:
            self.visited = True
        else:
            self.visited = False      

    # def add_image(self, input_image_url):
    #     self.image = input_image_url

