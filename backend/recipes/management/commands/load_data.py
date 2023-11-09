import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'import csv file into database'

    def handle(self, *args, **options):

        with open('./data/ingredients.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                try:
                    obj, created = Ingredient.objects.get_or_create(
                        name=row[0],
                        measurement_unit=row[1]
                    )
                    if not created:
                        print(f'Ингредиент {obj} уже был добавлен в базу')
                except Exception as error:
                    print(f'Ошибка {error}')
