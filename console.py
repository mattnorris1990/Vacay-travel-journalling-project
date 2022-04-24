from models.country import Country
import repositories.country_repository as country_repository

# country_repository.delete_all()

# country1 = Country("France", "images/placeholder_country_image.jpg")
# country_repository.save(country1)

# country2 = Country("Spain", "images/placeholder_country_image.jpg")
# country_repository.save(country2)

country3 = Country("Germany", "images/placeholder_country_image.jpg")
country_repository.save(country3)

# countries = country_repository.select_all()

# for country in countries:
#     print(country.__dict__)

# country = country_repository.select(25)

# print(country.__dict__)

# country_repository.delete(27)

