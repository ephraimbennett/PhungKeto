from fastapi import APIRouter, Request, Depends, Body

from fastapi.responses import HTMLResponse
from .templates import templates

router = APIRouter()

@router.get('/', response_class=HTMLResponse)
def home(request : Request):
    return templates.TemplateResponse("index.html", {'request': request})

@router.get('/about', response_class=HTMLResponse)
def about(request : Request):
    return templates.TemplateResponse("about.html", {'request': request})