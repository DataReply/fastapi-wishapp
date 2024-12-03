from fastapi import FastAPI

from routers import wishlists

app = FastAPI()

app.include_router(wishlists.router, prefix="/wishlists", tags=["wishlists"])
