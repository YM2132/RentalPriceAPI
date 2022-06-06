from rest_framework import generics

from .models import Rental
from .serializers import RentalSerializer

# Create your views here.
class RentalList(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class RentalDetail(generics.RetrieveAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
