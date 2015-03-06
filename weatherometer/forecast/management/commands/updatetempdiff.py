from django.core.management.base import BaseCommand, CommandError
from forecast.models import *
from forecast.forms import update_temp_diff

class Command(BaseCommand):
    help = """Updates the "differential" field of the weather ForecastItem model
    with how far off the forecast was from the actual temperature."""
    args = '[appname ...]'

    def handle(self, *app_labels, **options):
        from django.db.models import get_app, get_apps, get_models
        from django.conf import settings
        from datetime import datetime, timedelta
        update_temp_diff()
