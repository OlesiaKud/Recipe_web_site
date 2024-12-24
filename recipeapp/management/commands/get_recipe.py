from django.core.management.base import BaseCommand
from recipeapp.models import User, Recipe

class Command(BaseCommand):
    help = "Get all recipes by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            recipes = Recipe.objects.filter(user=user)
            intro = f'All recipes of {user.name}\n'
            text = '\n'.join(recipe.get_summary() for recipe in recipes)

            self.stdout.write(f'{intro}{text}')




# Проверить,