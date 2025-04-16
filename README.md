# URL Shortener

Un servicio de acortamiento de URLs simple y eficiente construido con FastAPI y Redis, que permite generar enlaces cortos con expiración automática después de 24 horas.

## Características

- Generación de URLs cortas con identificadores aleatorios de 8 caracteres
- Interfaz web amigable para acortar enlaces
- Expiración automática de enlaces después de 24 horas
- Manejo de enlaces caducados con página personalizada
- Alta escalabilidad gracias a Redis como almacenamiento

## Requisitos previos

- Python 3.8 o superior
- Redis (local o remoto)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/yourusername/shortener.git
   cd shortener
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
   
   O si prefieres usar uv:
   ```
   uv sync
   ```

3. Configura las variables de entorno:
   
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   
   ```
   # URL base del servicio (sin / al final)
   SERVER_URL=
   
   # Configuración de Redis
   REDIS_HOST=
   REDIS_PORT=
   REDIS_DB=
   REDIS_USERNAME=
   REDIS_PASSWORD=
   REDIS_USE_SSL=
   ```

## Uso

1. Inicia el servidor:
   ```
   uvicorn main:app --reload
   ```

2. Abre tu navegador y accede a:
   ```
   http://localhost:8000
   ```

3. Para acortar una URL mediante API:
   ```
   curl -X POST "http://localhost:8000/short/?original_url=https://ejemplo.com"
   ```

## Estructura del proyecto

```
├── config/
│   └── redis.py           # Configuración de la conexión a Redis
├── static/
│   └── logo-simple-negative-rb.png  # Logo para la interfaz web
├── templates/
│   ├── expired.html       # Plantilla para URLs expiradas
│   └── index.html         # Plantilla de la página principal
├── main.py                # Archivo principal de la aplicación
├── pyproject.toml         # Configuración del proyecto Python
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

## Tecnologías utilizadas

- **FastAPI**: Framework web de alto rendimiento
- **Redis**: Base de datos en memoria para almacenamiento de URLs
- **Jinja2**: Motor de plantillas para las páginas HTML
- **nanoid**: Generador de identificadores únicos

## Personalización

- El tiempo de expiración de las URLs puede modificarse ajustando la constante `TTL_SECONDS` en `config/redis.py`
- Las plantillas HTML en la carpeta `templates/` pueden personalizarse según las necesidades de diseño

## Licencia

Este proyecto está bajo la Licencia GNU V3. Ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invitame una cerveza 🍺 o un café ☕. 
* Da las gracias públicamente 🤓.

---
⌨️ con ❤️ por [TerciodeMarte](https://github.com/TerciodeMarte) 😊