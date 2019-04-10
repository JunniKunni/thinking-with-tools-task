from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from functools import reduce
import operator
from django.db.models import Q
from .models import *

def home(request):
    return render(request, 'CarData/map.html')

'''
Collects basic statistics for each car model for a given country
'''
def details(request, import_country):

    car_trans = CarTransaction.objects.all()
    curr_country_trans = car_trans.filter(import_country=import_country)

    car_details = {}

    for transaction in curr_country_trans:
        if transaction.car_model not in car_details:
            # Order in the list: Average, Min, Max, Count
            detail = []
            detail.append(transaction.sale_price)
            detail.append(transaction.sale_price)
            detail.append(transaction.sale_price)
            detail.append(1)
            car_details[transaction.car_model] = detail
        else:
            curr_car = car_details[transaction.car_model]
            # Calculating new Average
            average = ((curr_car[0] * curr_car[-1]) + transaction.sale_price) / ( curr_car[-1]+1 )
            curr_car[0] = average

            # Checking for min
            if curr_car[1] > transaction.sale_price:
                curr_car[1] = transaction.sale_price

            # Checking for max
            if curr_car[2] < transaction.sale_price:
                curr_car[2] = transaction.sale_price

            # Incrementing the count
            curr_car[-1] += 1

    context = {'country': import_country, 'car_details': car_details}

    return render(request, 'CarData/details.html', context)

'''
The search function receives a user input of a car model
This will then filter out every car except for that requested
Returns the results
'''
"""
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(car__model__icontains=query) | Q(make__icontains=query)

            results = CarTransaction.objects.filter(lookups).distinct()

            context ={'results': results,
                     'submit': submitbutton}

            return render(request, 'CarData/home.html', context)

        else:
            return render(request, 'CarData/home.html')

    else:
        return render(request, 'CarData/home.html')
"""