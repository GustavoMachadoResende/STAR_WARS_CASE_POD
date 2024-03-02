from fastapi import FastAPI
# from mangum import Mangum
from api.src.controller import router

app = FastAPI()
# handler = Mangum(app)

app.include_router(router)