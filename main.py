import os
from fastapi import FastAPI, HTTPException, Depends, Request
from nanoid import generate
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from redis import Redis

# Importar la conexión de Redis desde el módulo config
from config.redis import TTL_SECONDS, get_redis_client

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Configuración de los templates
templates = Jinja2Templates(directory="templates")

# Montar la carpeta de templates como directorio estático para servir imágenes
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    """
    Ruta principal que devuelve una página HTML con un formulario para acortar URLs
    """
    base_url = os.getenv('SERVER_URL', 'http://localhost:8000/')
    return templates.TemplateResponse("index.html", {"request": request,"BASE_URL": base_url})

@app.post("/short/")
def shorten_url(original_url: str, r: Redis = Depends(get_redis_client)):
    uid = generate(size=8)
    r.set(uid, original_url, ex=TTL_SECONDS)  # ex = expire time in seconds
    return {"short_url": os.getenv('SERVER_URL','http://localhost:8000/')+uid}

@app.get("/{uid}")
def redirect_url(uid: str, request: Request, r: Redis = Depends(get_redis_client)):
    original_url = r.get(uid)
    if not original_url:
        # Devolver la plantilla expired.html con código 404 cuando la URL no existe o ha expirado
        return templates.TemplateResponse("expired.html", {"request": request}, status_code=404)
    return RedirectResponse(original_url, status_code=307)
