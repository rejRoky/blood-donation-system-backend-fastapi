from fastapi import FastAPI
from app.routes import user_routes, area_routes, donation_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(area_routes.router)
app.include_router(donation_routes.router)
