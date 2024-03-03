import unittest
from src.repository import RepositoryStarWars


class TestRepositoryStarWars(unittest.TestCase):
    def setUp(self):
        self.repository = RepositoryStarWars(character='Yoda', planet='Tatooine', starship='Executor',  film='A New Hope')
        self.url = 'https://swapi.dev/api/people/20/'

    def test_get_data_from_swapi(self):
        result = self.repository._get_data_from_swapi(context='people', value='Yoda')
        result_complete_url = self.repository._get_data_from_swapi(complete_url=self.url)

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

    def test_get_data_of_complete_url_from_swapi(self):
        url_list = ['https://swapi.dev/api/people/1/', 'https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/']
        result_url_list = self.repository._get_data_of_complete_url_from_swapi(url=url_list, context='people')
        expected_result_url_list = ['Luke Skywalker', 'C-3PO', 'R2-D2']

        self.assertIsInstance(result_url_list, list)
        self.assertEqual(result_url_list, expected_result_url_list)

        result_url_str = self.repository._get_data_of_complete_url_from_swapi(url=self.url, context='people')
        expected_result_url_str = 'Yoda'

        self.assertIsInstance(result_url_str, str)
        self.assertEqual(result_url_str, expected_result_url_str)

    def test_get_character_data(self):
        result = self.repository._get_character_data()
        expected_result = {
            "Character - Yoda": {
                "name": "Yoda",
                "hair_color": "white",
                "skin_color": "green",
                "eye_color": "brown",
                "gender": "male",
                "birth_year": "896BBY",
                "home_planet": "unknown",
                "films": [
                "The Empire Strikes Back",
                "Return of the Jedi",
                "The Phantom Menace",
                "Attack of the Clones",
                "Revenge of the Sith"
                ],
                "starships": []
            }
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)

    def test_get_planet_data(self):
        result = self.repository._get_planet_data()
        expected_result = {
            "Planet - Tatooine": {
                "name": "Tatooine",
                "population": "200000",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "residents": [
                "Luke Skywalker",
                "C-3PO",
                "Darth Vader",
                "Owen Lars",
                "Beru Whitesun lars",
                "R5-D4",
                "Biggs Darklighter",
                "Anakin Skywalker",
                "Shmi Skywalker",
                "Cliegg Lars"
                ],
                "films": [
                "A New Hope",
                "Return of the Jedi",
                "The Phantom Menace",
                "Attack of the Clones",
                "Revenge of the Sith"
                ]
            }
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)

    def test_get_starship_data(self):
        result = self.repository._get_starship_data()
        expected_result = {
            "Starship - Executor": {
                "name": "Executor",
                "model": "Executor-class star dreadnought",
                "starship_class": "Star dreadnought",
                "passengers": "38000",
                "cost_in_credits": "1143350000",
                "length": "19000",
                "consumables": "6 years",
                "pilots": [],
                "films": [
                "The Empire Strikes Back",
                "Return of the Jedi"
                ]
            }
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)

    def test_get_film_data(self):
        result = self.repository._get_film_data()
        expected_result = {
            "Film - A New Hope": {
                "title": "A New Hope",
                "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25",
                "characters": [
                "Luke Skywalker",
                "C-3PO",
                "R2-D2",
                "Darth Vader",
                "Leia Organa",
                "Owen Lars",
                "Beru Whitesun lars",
                "R5-D4",
                "Biggs Darklighter",
                "Obi-Wan Kenobi",
                "Wilhuff Tarkin",
                "Chewbacca",
                "Han Solo",
                "Greedo",
                "Jabba Desilijic Tiure",
                "Wedge Antilles",
                "Jek Tono Porkins",
                "Raymus Antilles"
                ],
                "planets": [
                "Tatooine",
                "Alderaan",
                "Yavin IV"
                ],
                "starships": [
                "CR90 corvette",
                "Star Destroyer",
                "Sentinel-class landing craft",
                "Death Star",
                "Millennium Falcon",
                "Y-wing",
                "X-wing",
                "TIE Advanced x1"
                ]
            }
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()