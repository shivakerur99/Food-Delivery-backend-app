from django.urls import path
from .views import DeliveryCostAPIView
from .views import OrganizationCreateAPIView, ItemCreateAPIView
from .views import PricingCreateAPIView


urlpatterns = [
    path('organizations/', OrganizationCreateAPIView.as_view(), name='create_organization'),
    path('items/', ItemCreateAPIView.as_view(), name='create_item'),
    path('calculate-price/', DeliveryCostAPIView.as_view(), name='calculate_price'),
    path('pricing/', PricingCreateAPIView.as_view(), name='create_pricing'),
]