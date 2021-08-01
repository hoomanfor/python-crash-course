import unittest
from city_functions import get_formatted_location

class LocationsTestCase(unittest.TestCase):
    """Tests for 'get_formatted_location'."""

    def test_city_country(self):
        """Do cities and countries like 'Stockholm Sweden' work?"""

        formatted_location = get_formatted_location('stockholm', 'sweden')
        self.assertEqual(formatted_location, 'Stockholm, Sweden')

if __name__ == '__main__':
    unittest.main()