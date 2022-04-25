from unittest.util import _PLACEHOLDER_LEN
from models.country import Country
from models.place import Place
from models.country_entry import Country_Entry
import repositories.country_repository as country_repository
import repositories.place_repository as place_repository
import repositories.country_entry_repository as country_entry_repository

# country_entry_repository.delete_all()
# place_repository.delete_all()
# country_repository.delete_all()


# country1 = Country("France", "images/placeholder_country_image.jpg")
# country_repository.save(country1)

# country2 = Country("Spain", "images/placeholder_country_image.jpg")
# country_repository.save(country2)

# country3 = Country("Germany", "images/placeholder_country_image.jpg", True)
# country_repository.save(country3)

# countries = country_repository.select_all()

# for country in countries:
#     print(country.__dict__)

# country = country_repository.select(25)

# print(country.__dict__)

# country_repository.delete(27)

# country3 = Country("Italy", "images/placeholder_country_image.jpg", "True", 3)
# country_repository.update(country3)

# place1 = Place("Paris", country1, "images/placeholder_country_image.jpg")
# place_repository.save(place1)

# place2 = Place("Berlin", country3, "images/placeholder_country_image.jpg")
# place_repository.save(place2)

# place3 = Place("Hamburg", country3, "images/placeholder_country_image.jpg")
# place_repository.save(place3)

# places = place_repository.select_all()

# for place in places:
#     print(place.__dict__)

# place = place_repository.select(2)

# print(place.__dict__)

# place3 = Place("Cologne", country3, "images/placeholder_country_image.jpg", True, 3)
# place_repository.update(place3)

# country_entry1 = Country_Entry("Test Title", "This is a test entry", "images/placeholder_country_image.jpg", country1)
# country_entry_repository.save(country_entry1)

# country_entry2 = Country_Entry("2nd test title", "This is another test entry", "images/placeholder_country_image.jpg", country2)
# country_entry_repository.save(country_entry2)

# country_entries = country_entry_repository.select_all()

# for entry in country_entries:
#     print(entry.__dict__)

entry = country_entry_repository.select(5)

print(entry.__dict__)