from fastapi import FastAPI

from app.database import create_tables
from app.routers import wishlists, auth, users


create_tables()

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(wishlists.router, prefix="/wishlists", tags=["wishlists"])
