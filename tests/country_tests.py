import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country("Scotland", "placeholder_country_image", "Europe", True, 1)
        self.country2 = Country("Wales", "placeholder_country_image", "Europe", False, 2)

    def test_update_visit_status(self):
        self.country1.update_country_visit_status(self.country1)
        self.assertEqual(False, self.country1.visited)