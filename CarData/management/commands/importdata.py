"""
Import json data from URL to Database
"""
import requests
import json
import sys
from CarData.models import CarTransaction, Country # Import your model here
from django.core.management.base import BaseCommand

# URL to import from with field
IMPORT_URL = 'https://my.api.mockaroo.com/jkim.json?key=e6ac1da0&countries='

class Command(BaseCommand):

    # adding user input for countries
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('countries_inp', type=str)


    # To create an instance of a transaction
    def import_cartransaction(self, data):

        car_id = data.get('id', None)
        import_country = data.get('import_country', None)
        car_model = data.get('model', None)
        make = data.get('make', None)
        sold_by = data.get('sold_by', None)
        sale_price = data.get('sale_price', None)


        try:  # try and catch for saving the objects

            # To ensure there are no additional repeating data points

            transaction, created_tran = CarTransaction.objects.get_or_create(
                car_id=car_id,
                import_country=import_country,
                car_model=car_model,
                make=make,
                sold_by=sold_by,
                sale_price=sale_price
            )
            country, created_coun = Country.objects.get_or_create(
                country=import_country
            )
            if created_tran:
                transaction.save()
            display_format = "\nCar Transaction saved."
            print(display_format.format(transaction))


        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong!\n{}".format(car_id, str(ex))
            print(msg)


    # Makes the GET request to the api
    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL + options['countries_inp'],
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()
        for data_object in data:
            self.import_cartransaction(data_object)
        print(IMPORT_URL + options['countries_inp'])