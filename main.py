from fastapi import FastAPI

from api import users, etablissements, category, services
from db.db_setup import engine
from db.models import User, Etablissement, Category, Service
 
User.Base.metadata.create_all(bind=engine)
Etablissement.Base.metadata.create_all(bind=engine)
Category.Base.metadata.create_all(bind=engine)
Service.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="API basique",
    version="1",
    terms_of_service="http//www.example.com/terms",
    contact={
        "name": "Loic",
        "email": "loic@mail.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(users.router)
app.include_router(etablissements.router)
app.include_router(category.router)
app.include_router(services.router)
