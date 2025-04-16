import redis
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

TTL_SECONDS = 60*60*24  # 24 hours in seconds (24 * 60 * 60)

def get_redis_connection():
    """
    Crea y retorna una conexión a Redis utilizando variables de entorno para la configuración
    """
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        db=int(os.getenv('REDIS_DB', 0)),
        username=os.getenv('REDIS_USERNAME', ''),
        password=os.getenv('REDIS_PASSWORD', ''),
        decode_responses=True,
        ssl=True if os.getenv('REDIS_USE_SSL', 'false').lower() == 'true' else False,
    )

def get_redis_client():
    """
    Dependency que provee una conexión a Redis usando el gestor de contexto.
    """
    with RedisConnection() as redis_client:
        yield redis_client
        # La conexión se cerrará automáticamente al finalizar el endpoint

class RedisConnection:
    """
    Gestor de contexto para conexiones a Redis.
    Garantiza que la conexión se cierre al finalizar el bloque 'with'.
    """
    def __init__(self):
        self.redis_client = None
        
    def __enter__(self):
        self.redis_client = get_redis_connection()
        return self.redis_client
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.redis_client:
            self.redis_client.close()