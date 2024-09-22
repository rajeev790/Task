from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone

class Order(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_customers(cls):
        six_months_ago = timezone.now() - timedelta(days=6 * 30)
        return cls.objects.filter(order_date__gte=six_months_ago).values('customer').annotate(total_spent=Sum('total_amount')).order_by('-total_spent')[:5]

# View Example
from django.http import JsonResponse
from .models import Order

def top_customers_view(request):
    customers = Order.top_customers()
    return JsonResponse(list(customers), safe=False)
