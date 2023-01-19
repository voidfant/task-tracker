from routers import oauth, route
from db import models
from db.database import engine

from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route.router)
app.include_router(oauth.router)


@app.get("/")
async def root():
    return {"message": "ligma!"}
