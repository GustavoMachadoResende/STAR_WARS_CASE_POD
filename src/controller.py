# controller.py
from fastapi import APIRouter
import requests

router = APIRouter()

class Controller:
    # def __init__(self) -> None:
    #     self.name = "Gustavo"

    @router.get("/test")
    def controller_test(name: str) -> None:
        try:
            url: str =  f'https://swapi.dev/api/{name}/'
            url_connection = requests.get(url)
            test = url_connection 
            return test
        except Exception as e:
            raise e