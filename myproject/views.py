from django.http import JsonResponse
from .models import Order

def top_customers_view(request):
    customers = Order.top_customers()
    return JsonResponse(list(customers), safe=False)
