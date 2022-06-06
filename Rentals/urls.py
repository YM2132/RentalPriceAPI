from django.urls import path
from .views import RentalDetail, RentalList

urlpatterns = [
    path('<int:pk>/', RentalDetail.as_view(), name='rental_detail'),
    path('', RentalList.as_view(), name='rental_list')
]
