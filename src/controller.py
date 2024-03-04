from typing import Optional
from fastapi import APIRouter, HTTPException
from src.repository import RepositoryStarWars

router = APIRouter()

@router.get("/starwars-data", tags=["Star Wars"])
def controller_get_all_about_star_wars(character: Optional[str] = None, planet: Optional[str] = None, starship: Optional[str] = None, film: Optional[str] = None):
    try:
        if not any([character, planet, starship, film]):
            raise HTTPException(status_code=400, detail={
                'message': 'Please search for at least one of the fields to get your Star Wars information.',
            })

        repository: RepositoryStarWars = RepositoryStarWars(character=character, planet=planet, starship=starship, film=film)
        result: dict = repository.get_all_star_wars_data()

        return result
    except Exception as e:
        raise e