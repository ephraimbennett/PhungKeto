from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_proxiedheadersmiddleware import ProxiedHeadersMiddleware


from .routes import router

app = FastAPI()

# Add middleware
app.add_middleware(ProxiedHeadersMiddleware)

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


