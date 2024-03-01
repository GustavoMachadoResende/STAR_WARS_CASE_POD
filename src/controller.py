# controller.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def controller_test():
    test = 'oi'
    return test