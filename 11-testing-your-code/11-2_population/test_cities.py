import unittest
from city_functions import get_formatted_location

class LocationsTestCase(unittest.TestCase):
    """Tests for 'get_formatted_location'."""

    def test_city_country(self):
        """Do cities and countries like 'Stockholm Sweden' work?"""

        formatted_location = get_formatted_location('stockholm', 'sweden')
        self.assertEqual(formatted_location, 'Stockholm, Sweden')
    
    def test_city_country_population(self):
        """Do cities, countries, and populations like 'Stockholm Sweden 975000' work?"""

        formatted_location = get_formatted_location('stockholm', 'sweden', 975000)
        self.assertEqual(formatted_location, 'Stockholm, Sweden - population 975000.')

if __name__ == '__main__':
    unittest.main()