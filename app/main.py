from fastapi import FastAPI

from app.breed.router import router as breed_router
from app.kitten.router import router as kitten_router

description = """REST API для администратора онлайн выставки котят"""


app: FastAPI = FastAPI(
    title="FastAPI breeds of kittens API",
    description=description,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Support Team",
        "url": "http://example.com/contact/",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(breed_router)
app.include_router(kitten_router)
