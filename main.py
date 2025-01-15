from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configurar el directorio de plantillas
templates = Jinja2Templates(directory="templates")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ejemplo de servicios
services = [
    {
        "name": "Clases Grupales",
        "description": "Ofrecemos clases grupales como yoga, pilates, spinning y más.",
        "image": "/static/images/services.jpg"
    },
    {
        "name": "Entrenamiento Personal",
        "description": "Obtén un plan de entrenamiento personalizado con nuestros entrenadores profesionales.",
        "image": "/static/images/services.jpg"
    },
    {
        "name": "Zonas de Cardio y Pesas",
        "description": "Disponemos de las mejores instalaciones y equipos para tus entrenamientos de cardio y pesas.",
        "image": "/static/images/services.jpg"
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Bienvenido a SPORTACUS.GYM", "services": services})

@app.post("/send-message")
async def send_message(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Aquí puedes procesar el mensaje como enviar un correo electrónico o guardarlo en una base de datos
    print(f"Nombre: {name}, Email: {email}, Mensaje: {message}")
    return templates.TemplateResponse("index.html", {"request": request, "title": "Bienvenido a SPORTACUS.GYM", "services": services, "msg": "Mensaje enviado correctamente"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)