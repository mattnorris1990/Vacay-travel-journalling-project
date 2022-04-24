class City:

    def __init__(self, input_name, input_visited = False, input_last_date_visited = None):
        self.name = input_name
        self.visited = input_visited
        self.last_date_visited = input_last_date_visited
        self.image = None

    def mark_visited(self):
        if self.visited == False:
            self.visited = True
        else:
            self.visited == False      

    def add_image(self, input_image_url):
        self.image = input_image_url