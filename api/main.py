from fastapi import FastAPI
from mangum import Mangum
from api.src.controller import router

app = FastAPI()
app.include_router(router)

handler = Mangum(app)