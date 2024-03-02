from fastapi import APIRouter
import requests
from api.src.repository import soma

router = APIRouter()

@router.get("/soma")
# def controller_test(name: str) -> None:
def controller_test(num1, num2) -> None:
    try:
        # url: str =  f'https://swapi.dev/api/{name}/'
        # url_connection = requests.get(url)
        # test = url_connection
        soma_test = soma(num1, num2)
        result = {"soma": soma_test}
        return result
    except Exception as e:
        raise e