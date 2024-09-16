from rest_framework.decorators import api_view , permission_classes 
from rest_framework.response import Response
from rest_framework import status
from truck.models import Truck
from truck.serializers import TruckSerializer
from .permissions import IsAdminUser 



# create a truck only by the admin
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_truck(request):
    try:
        serializer = TruckSerializer(data=request.data) 
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"data saved":serializer.data},status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "Invalid data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)       
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(["GET"])
def get_trucks(request):
    trucks = Truck.objects.all()
    serializer = TruckSerializer(trucks,many=True)
    return Response({"sucess":serializer.data},status=status.HTTP_200_OK)