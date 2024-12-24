import random
from random import choices
from django.core.management.base import BaseCommand
from recipeapp.models import User,Recipe

LOREM = ("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa."
         " Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, "
         "ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, "
         "fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae,"
         " justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper "
         "nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim."
         " Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius"
         " laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies"
         "nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero,"
         " sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem."
         " Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante."
         " Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. "
         "Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,")


class Command(BaseCommand):
    help = "Generate test users and recipes."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            autor = User(name=f'User_{i}', email=f'mail{i}@mail.ru')
            autor.save()
        for j in range(1, count + 1):
            recipe = Recipe(
                name=f'Title-{j}',
                description=" ".join(choices(text, k=20)),
                autor=autor,
                steps_cooking=" ".join(choices(text, k=100)),
                time_cooking=f'{random.randint(2,60)} minutes',
            )
            recipe.save()
