from django.core.management.base import BaseCommand
from store.models import Product
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the products table with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create a batch of 20 fake products
        for _ in range(20):
            Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200),
                price=fake.random_number(digits=2),
                stock=fake.random_int(min=1, max=100),
                image_url=fake.image_url(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 20 products'))
