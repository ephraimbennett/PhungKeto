from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles


from .routes import router

app = FastAPI()

# Register static files directories
app.mount(
    "/app/static", StaticFiles(directory="app/static"), name="static"
)


# Register the routers
app.include_router(
    router,           # reference the router object
    prefix="",               # optional prefix for all endpoints here
    tags=["home"]                 # groups them in the docs
)


