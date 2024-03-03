#VOLTAR DO FOR PARA PASSAR PELAS URLS DO ARRAY
import json
from fastapi import HTTPException
import requests
class RepositoryStarWars:
    def __init__(self, character: str, planet, starship: str, film: str) -> None:
        self.character = character
        self.planet = planet
        self.starship = starship
        self.film = film

    def get_data_from_swapi(self, context: str = None, value: str = None, complete_url: str = None):
        try:
            if complete_url:
                response = requests.get(complete_url)
                data = response.json()
                return data
            else:
                url = f'https://swapi.dev/api/{context}/?search={value}'
                response = requests.get(url)
                data = response.json()
                if data['count'] == 0:
                    raise HTTPException(status_code=404, detail={
                        'message': f'The {context} {value} does not exist in Star Wars.',
                    })
                return data['results'][0]
        except Exception as e:
             raise e

    def get_character_data(self, character: str):
        try:
            character_data = self.get_data_from_swapi(context='people', value=character)
            dict_name =  f"Character - {character_data['name']}"
            character_data_dict = {
                dict_name: {
                    'name': character_data['name'],
                    'hair_color': character_data['hair_color'],
                    'skin_color': character_data['skin_color'],
                    'eye_color': character_data['eye_color'],
                    'gender': character_data['gender'],
                    'birth_year': character_data['birth_year'],
                    'home_planet': self.get_data_of_complete_url(url=character_data['homeworld'], context='planets'),
                    'films': self.get_data_of_complete_url(url=character_data['films'], context='films'),
                    'starships': self.get_data_of_complete_url(url=character_data['starships'], context='starships')
                }
            }
            return character_data_dict
        except Exception as e:
                raise e

    def get_planet_data(self, planet: str):
        try:
            planet_data = self.get_data_from_swapi(context='planets', value=planet)
            dict_name =  f"Planet - {planet_data['name']}"
            planet_data_dict = {
                dict_name: {
                    'name': planet_data['name'],
                    'population': planet_data['population'],
                    'climate': planet_data['climate'],
                    'gravity': planet_data['gravity'],
                    'terrain': planet_data['terrain'],
                    'residents': self.get_data_of_complete_url(url=planet_data['residents'], context='people'),
                    'films': self.get_data_of_complete_url(url=planet_data['films'], context='films')
                    # TODO ver de colocar as pessoas
                }
            }
            return planet_data_dict
        except Exception as e:
                raise e

    def get_starship_data(self, starship: str):
        try:
            starship_data = self.get_data_from_swapi(context='starships', value=starship)
            dict_name =  f"Starship - {starship_data['name']}"
            starship_data_dict = {
                dict_name: {
                    'name': starship_data['name'],
                    'model': starship_data['model'],
                    'starship_class': starship_data['starship_class'],
                    'passengers': starship_data['passengers'],
                    'cost_in_credits': starship_data['cost_in_credits'],
                    'length': starship_data['length'],
                    'consumables': starship_data['consumables'],
                    'pilots': self.get_data_of_complete_url(url=starship_data['pilots'], context='people'),
                    'films': self.get_data_of_complete_url(url=starship_data['films'], context='films')
                }
            }
            return starship_data_dict
        except Exception as e:
                raise e

    def get_film_data(self, film: str):
        try:
            film_data = self.get_data_from_swapi(context='films', value=film)
            dict_name =  f"Film - {film_data['title']}"
            film_data_dict = {
                dict_name: {
                    'title': film_data['title'],
                    'opening_crawl': film_data['opening_crawl'],
                    'director': film_data['director'],
                    'producer': film_data['producer'],
                    'release_date': film_data['release_date'],
                    'characters': self.get_data_of_complete_url(url=film_data['characters'], context='people'),
                    'planets': self.get_data_of_complete_url(url=film_data['planets'], context='planets'),
                    'starships': self.get_data_of_complete_url(url=film_data['starships'], context='starships')
                }
            }
            return film_data_dict
        except Exception as e:
                raise e

    def get_data_of_complete_url(self, url: list|str, context: str):
        try:
            if isinstance(url, list):
                data_list = ([])
                for url_item in url:
                    data = self.get_data_from_swapi(complete_url=url_item)
                    if context == 'films':
                        data_list.append(data['title'])
                    else:
                        data_list.append(data['name'])
                return data_list

            if isinstance(url, str):
                 data = self.get_data_from_swapi(complete_url=url)
                 return data['name']
        except Exception as e:
            raise e

    def all_data_about_star_wars(self):
        try:
            data_list = ([])

            if self.character and isinstance(self.character, str):
                character_data = self.get_character_data(character=self.character)
                data_list.append(character_data)

            if self.planet and isinstance(self.planet, str):
                planet_data = self.get_planet_data(planet=self.planet)
                data_list.append(planet_data)

            if self.starship and isinstance(self.starship, str):
                starship_data = self.get_starship_data(starship=self.starship)
                data_list.append(starship_data)

            if self.film and isinstance(self.film, str):
                film_data = self.get_film_data(film=self.film)
                data_list.append(film_data)

            if not self.character and not self.planet and not self.starship and not self.film:
                raise HTTPException(status_code=400, detail={
                    'message': 'Please search for at least one of the fields to get your Star Wars information.',
                })

            json_string = json.dumps(data_list)
            json_result = json.loads(json_string)

            return json_result
        except Exception as e:
                raise e