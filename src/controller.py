from typing import Optional
from fastapi import APIRouter
from src.repository import RepositoryStarWars

router = APIRouter()

@router.get("/starwars-data")
def controller_get_all_about_star_wars(character: Optional[str] = None, planet: Optional[str] = None, starship: Optional[str] = None, film: Optional[str] = None):
    try:
        repository: RepositoryStarWars = RepositoryStarWars(character=character, planet=planet, starship=starship, film=film)
        result: dict = repository.get_all_star_wars_data()

        return result
    except Exception as e:
        raise e