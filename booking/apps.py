from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    Primary Key for booking app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
