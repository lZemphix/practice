from django.shortcuts import render
from discounts.models import Discount
# Create your views here.

def index(request):
    return render(request, 'discounts/index.html')

def discounts(request): #TODO: context from database
    context = {'discounts': Discount.objects.all()}
    return render(request, 'discounts/discounts.html', context=context)