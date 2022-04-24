from models.country import Country
import repositories.country_repository as country_repository

country1 = Country("France")
country_repository.save(country1)