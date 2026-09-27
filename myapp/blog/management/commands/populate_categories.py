from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Category.objects.all().delete()

        categories = ['SPORTS', 'TECHNOLOGY', 'SCIENCE', 'ART', 'FOOD']

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Successfully inserted 5 categories"))