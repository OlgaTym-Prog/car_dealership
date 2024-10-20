from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car
from main.models import Sale


def cars_list_view(request):
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': Car.objects.all()})


def car_details_view(request, car_id):
    template_name = 'main/details.html'
    car = get_object_or_404(Car, id=car_id)
    return render(request, template_name, {'car': car})


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})
    except Car.DoesNotExist:
        raise Http404('Car not found')
