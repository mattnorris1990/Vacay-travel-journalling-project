from unittest.util import _PLACEHOLDER_LEN
from models.country import Country
from models.place import Place
import repositories.country_repository as country_repository
import repositories.place_repository as place_repository

country_repository.delete_all()

country1 = Country("France", "images/placeholder_country_image.jpg")
country_repository.save(country1)

country2 = Country("Spain", "images/placeholder_country_image.jpg")
country_repository.save(country2)

country3 = Country("Germany", "images/placeholder_country_image.jpg")
country_repository.save(country3)

# countries = country_repository.select_all()

# for country in countries:
#     print(country.__dict__)

# country = country_repository.select(25)

# print(country.__dict__)

# country_repository.delete(27)

# country3 = Country("Italy", "images/placeholder_country_image.jpg", "True", 28)
# country_repository.update(country3)

# place1 = Place("Paris", country1, "images/placeholder_country_image.jpg")
# place_repository.save(place1)