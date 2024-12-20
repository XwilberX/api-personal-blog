from .config import Settings
import importlib

# Inicializa las configuraciones con Pydantic
settings = Settings()

# Carga dinámica de modelos
for app in settings.INSTALLED_APPS:
    try:
        importlib.import_module(f"{app}.{settings.MODEL_FILE_NAME[:-3]}")  # Cargar app.models
    except ModuleNotFoundError as e:
        print(f"Error al cargar modelos desde {app}: {e}")