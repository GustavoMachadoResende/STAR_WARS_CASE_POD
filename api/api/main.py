from fastapi import FastAPI
from mangum import Mangum
# from api.controller import router

app = FastAPI()
# app.include_router(router)

@app.get("/")
def controller_test() -> None:
    try:
        result = {"teste": "brabo"}
        return result
    except Exception as e:
        raise e
    
handler = Mangum(app)