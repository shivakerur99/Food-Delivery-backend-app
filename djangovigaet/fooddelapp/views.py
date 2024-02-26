from rest_framework.views import APIView
from rest_framework.response import Response
from .service import PriceCalculator

class DeliveryCostAPIView(APIView):
    def post(self, request):
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')

        if not all([zone, organization_id, total_distance, item_type]):
            return Response({'error': 'Missing required parameters'}, status=400)

        try:
            total_price = PriceCalculator.calculate_price(zone, organization_id, total_distance, item_type)
            if total_price is None:
                return Response({'error': 'Price not found for the given parameters'}, status=404)
            return Response({'total_price': total_price}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

from rest_framework import status
# from .models import Organization, Item
from .serializers import OrganizationSerializer, ItemSerializer,PricingSerializer

class OrganizationCreateAPIView(APIView):
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemCreateAPIView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PricingCreateAPIView(APIView):
    def post(self, request):
        serializer = PricingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)