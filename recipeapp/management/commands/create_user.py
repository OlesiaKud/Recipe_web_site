from django.core.management.base import BaseCommand
from recipeapp.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        user = User(name='Иванов', email='ivan@example.com', password='secret')
        user.save()
        self.stdout.write(f'{user}')




# сделать возможность автоматического добавления пользователя