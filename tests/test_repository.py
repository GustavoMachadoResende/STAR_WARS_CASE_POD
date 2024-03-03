import unittest
from src.repository import RepositoryStarWars


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = RepositoryStarWars(character='Yoda', planet='Tatooine', starship='Executor',  film='A New Hope')

    def test_get_data_from_swapi(self):
        result = self.repository._get_data_from_swapi(context='people', value='Yoda')
        result_complete_url = self.repository._get_data_from_swapi(complete_url='https://swapi.dev/api/people/20/')

        expected_result = {
            'name': 'Yoda',
            'height': '66',
            'mass': '17',
            'hair_color': 'white',
            'skin_color': 'green',
            'eye_color': 'brown',
            'birth_year': '896BBY',
            'gender': 'male',
            'homeworld': 'https://swapi.dev/api/planets/28/',
            'films': ['https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
            'species': ['https://swapi.dev/api/species/6/'],
            'vehicles': [],
            'starships': [],
            'created': '2014-12-15T12:26:01.042000Z',
            'edited': '2014-12-20T21:17:50.345000Z',
            'url': 'https://swapi.dev/api/people/20/'
        }
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result_complete_url, dict)
        self.assertEqual(result, expected_result)
        self.assertEqual(result_complete_url, expected_result)

if __name__ == '__main__':
    unittest.main()