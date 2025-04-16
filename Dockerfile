FROM python:3.11-slim

# Establecer directorio de trabajo en /app
WORKDIR /app

# Copiar archivos de requisitos primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
# Host 0.0.0.0 permite conexiones desde cualquier IP
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]