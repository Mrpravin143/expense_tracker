from django.core.management.base import BaseCommand
from home.models import News  
from datetime import datetime

class Command(BaseCommand):
    help = 'प्रत्येक मिनिटाला एक नवीन News तयार करते'

    def handle(self, *args, **kwargs):
        now = datetime.now()
        News.objects.create(
            title=f'Auto News at {now.strftime("%H:%M:%S")}',
            content='ही News cron job ने तयार केली आहे.',
        )
        self.stdout.write(self.style.SUCCESS("नवीन News तयार झाली!"))
