from django.core.management.base import BaseCommand
from recipeapp.models import User, Recipe


class Command(BaseCommand):
    help = "Create new recipe."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')



# Доработать, сделать создание  рецепта