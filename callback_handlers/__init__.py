from .historical import register_db_temperature_callbacks
from .live import register_callbacks_live

def register_callbacks(app):
    register_db_temperature_callbacks(app)
    register_callbacks_live(app)
