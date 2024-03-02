from fastapi import FastAPI
# from mangum import Mangum # TESTE
from api.src.controller import router

app = FastAPI()
# handler = Mangum(app)

app.include_router(router)