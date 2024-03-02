from fastapi import APIRouter
import requests
from src.repository import soma

router = APIRouter()

@router.get("/")
# def controller_test(name: str) -> None:
# def controller_test(num1, num2) -> None:
def controller_test() -> None:
    try:
        # url: str =  f'https://swapi.dev/api/{name}/'
        # url_connection = requests.get(url)
        # test = url_connection
        # soma_test = soma(num1, num2)
        result = {"teste": "brabo"}
        return result
    except Exception as e:
        raise e