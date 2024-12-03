from fastapi import FastAPI

from app.routers import wishlists, auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(wishlists.router, prefix="/wishlists", tags=["wishlists"])
