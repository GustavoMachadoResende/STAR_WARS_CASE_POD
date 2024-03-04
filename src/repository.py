import requests
from fastapi import HTTPException
class RepositoryStarWars:
    def __init__(self, character: str, planet: str, starship: str, film: str) -> None:
        self.character: str = character
        self.planet: str = planet
        self.starship: str = starship
        self.film: str = film

    def _get_data_from_swapi(self, context: str = None, value: str = None, complete_url: str = None) -> dict:
        try:
            if complete_url:
                response: requests.models.Response = requests.get(complete_url)
                data: dict = response.json()
                return data
            else:
                url: str = f'https://swapi.dev/api/{context}/?search={value}'
                response: requests.models.Response = requests.get(url)
                data: dict = response.json()
                if data['count'] == 0:
                    raise HTTPException(status_code=404, detail={
                        'message': f'The {context} {value} does not exist in Star Wars.',
                    })
                return data['results'][0]
        except Exception as e:
             raise e

    def _get_data_of_complete_url_from_swapi(self, url: list|str, context: str) -> list|str:
        try:
            if isinstance(url, list):
                data_list: list = ([])
                for url_item in url:
                    data: dict = self._get_data_from_swapi(complete_url=url_item)
                    if context == 'films':
                        data_list.append(data['title'])
                    else:
                        data_list.append(data['name'])
                return data_list

            if isinstance(url, str):
                 data: dict = self._get_data_from_swapi(complete_url=url)
                 return data['name']
        except Exception as e:
            raise e

    def _get_character_data(self) -> dict:
        try:
            character_data: dict = self._get_data_from_swapi(context='people', value=self.character)
            dict_name: str = f"Character - {character_data['name']}"
            character_data_dict: dict = {
                dict_name: {
                    'name': character_data['name'],
                    'hair_color': character_data['hair_color'],
                    'skin_color': character_data['skin_color'],
                    'eye_color': character_data['eye_color'],
                    'gender': character_data['gender'],
                    'birth_year': character_data['birth_year'],
                    'home_planet': self._get_data_of_complete_url_from_swapi(url=character_data['homeworld'], context='planets'),
                    'films': self._get_data_of_complete_url_from_swapi(url=character_data['films'], context='films'),
                    'starships': self._get_data_of_complete_url_from_swapi(url=character_data['starships'], context='starships')
                }
            }
            return character_data_dict
        except Exception as e:
                raise e

    def _get_planet_data(self) -> dict:
        try:
            planet_data: dict = self._get_data_from_swapi(context='planets', value=self.planet)
            dict_name: str = f"Planet - {planet_data['name']}"
            planet_data_dict: dict = {
                dict_name: {
                    'name': planet_data['name'],
                    'population': planet_data['population'],
                    'climate': planet_data['climate'],
                    'gravity': planet_data['gravity'],
                    'terrain': planet_data['terrain'],
                    'residents': self._get_data_of_complete_url_from_swapi(url=planet_data['residents'], context='people'),
                    'films': self._get_data_of_complete_url_from_swapi(url=planet_data['films'], context='films')
                }
            }
            return planet_data_dict
        except Exception as e:
                raise e

    def _get_starship_data(self) -> dict:
        try:
            starship_data: dict = self._get_data_from_swapi(context='starships', value=self.starship)
            dict_name: str = f"Starship - {starship_data['name']}"
            starship_data_dict: dict = {
                dict_name: {
                    'name': starship_data['name'],
                    'model': starship_data['model'],
                    'starship_class': starship_data['starship_class'],
                    'passengers': starship_data['passengers'],
                    'cost_in_credits': starship_data['cost_in_credits'],
                    'length': starship_data['length'],
                    'consumables': starship_data['consumables'],
                    'pilots': self._get_data_of_complete_url_from_swapi(url=starship_data['pilots'], context='people'),
                    'films': self._get_data_of_complete_url_from_swapi(url=starship_data['films'], context='films')
                }
            }
            return starship_data_dict
        except Exception as e:
                raise e

    def _get_film_data(self):
        try:
            film_data: dict = self._get_data_from_swapi(context='films', value=self.film)
            dict_name: str = f"Film - {film_data['title']}"
            film_data_dict: dict = {
                dict_name: {
                    'title': film_data['title'],
                    'opening_crawl': film_data['opening_crawl'],
                    'director': film_data['director'],
                    'producer': film_data['producer'],
                    'release_date': film_data['release_date'],
                    'characters': self._get_data_of_complete_url_from_swapi(url=film_data['characters'], context='people'),
                    'planets': self._get_data_of_complete_url_from_swapi(url=film_data['planets'], context='planets'),
                    'starships': self._get_data_of_complete_url_from_swapi(url=film_data['starships'], context='starships')
                }
            }
            return film_data_dict
        except Exception as e:
                raise e

    def get_all_star_wars_data(self) -> dict:
        try:
            result: dict = ({})

            if self.character and isinstance(self.character, str):
                character_data: dict = self._get_character_data()
                result.update(character_data)
                character_data = None

            if self.planet and isinstance(self.planet, str):
                planet_data: dict = self._get_planet_data()
                result.update(planet_data)
                planet_data = None

            if self.starship and isinstance(self.starship, str):
                starship_data: dict = self._get_starship_data()
                result.update(starship_data)
                starship_data = None

            if self.film and isinstance(self.film, str):
                film_data: dict = self._get_film_data()
                result.update(film_data)
                film_data = None

            return result
        except Exception as e:
                raise e