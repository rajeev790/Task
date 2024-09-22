from django.urls import path
from .views import top_customers_view

urlpatterns = [
    # URL to view top 5 customers
    path('top-customers/', top_customers_view),
]
