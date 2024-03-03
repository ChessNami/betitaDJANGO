from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required (optional)
from .models import Car, Rental
from datetime import date
from Templates import car_detail
from Templates import car_list

def car_list(request):
  available_cars = Car.objects.filter(is_available=True)
  return render(request, 'cars/car_list.html', {'cars': available_cars})

@login_required (optional=True)  # Allow both logged-in and anonymous users
def car_detail(request, pk):
  car = get_object_or_404(Car, pk=pk)
  # Check car availability for requested dates (optional)
  if request.method == 'POST':
    rental_start_date = request.POST.get('rental_start_date')
    rental_end_date = request.POST.get('rental_end_date')
    # Validate and process rental request (consider user authentication if implemented)
    if is_valid_rental_request(rental_start_date, rental_end_date, car):
      # Create a rental record (consider user association if implemented)
      rental = Rental.objects.create(car=car, customer_name=request.POST.get('customer_name'), 
                                     rental_start_date=rental_start_date, rental_end_date=rental_end_date)
      car.is_available = False
      car.save()
      return redirect('rental_confirmation', pk=rental.pk)  # Redirect to confirmation page
  return render(request, 'cars/car_detail.html', {'car': car})

def is_valid_rental_request(rental_
