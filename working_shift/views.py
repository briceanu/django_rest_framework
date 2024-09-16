
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.db.models import Q,F
from django.db.models import Sum
from working_shift.models import WorkingDayModel
from working_shift.serializer import LimitedWorkingDayModelSerializer, SerializerWorkingDayModel

# Create your views here.


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def save_working_day(request):
    try:
        serializer = SerializerWorkingDayModel(data=request.data)
        username_from_req = request.data.get('username')
        token = request.headers.get('Authorization')
        if not token or not token.startswith("Bearer "):
            return Response({"error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")[1]
        validate_token = AccessToken(token)

            # Extract username from the token
        username = validate_token['username']
   
        if username != username_from_req:
            return Response({"error":"username does't match with the login credentials"}
                            ,status=status.HTTP_400_BAD_REQUEST)  
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"success": f"data saved {serializer.data}"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "Invalid data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(["GET"])
def get_day(request):
    trucks = WorkingDayModel.objects.all()
    serializer = SerializerWorkingDayModel(trucks,many=True)
    return Response({"sucess":serializer.data},status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_load(request):
    try:
        drivers = WorkingDayModel.objects.filter(km_driven__lte=550)
        if drivers is None:
            return Response({"error":"no drivers match the criteria"},status=status.HTTP_204_NO_CONTENT)
            
        seralizer = SerializerWorkingDayModel(drivers,many=True)
        return Response({"success":seralizer.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(["GET"])
def get_data(request):
    try:
        km = request.query_params.get('km')
        registation_plate = request.query_params.get('registration_plate')

        if not km or not registation_plate:
            return Response({"error":"km or registration plate not provided"},status=status.HTTP_400_BAD_REQUEST)

        trucks = WorkingDayModel.objects.filter(
            Q(truck_used=registation_plate)&
            Q(km_driven__lte=km))

        if trucks is None:
            return Response({"error":"no trucks matching the criteria"},status=status.HTTP_204_NO_CONTENT)
        serializer = LimitedWorkingDayModelSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@api_view(["GET"])
def get_km(request):
    try:
        registration_plate = request.query_params.get('registration_plate')
        req_username = request.query_params.get('username')  # Retrieve the username parameter

        if not registration_plate or not req_username:
            return Response({"error": "Registration plate or username not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        total_km = WorkingDayModel.objects.filter(
            Q(truck_used=registration_plate) &
            Q(username=req_username)
        ).aggregate(total_km=Sum('km_driven'), total_fuel=Sum('fuel_consumption'))

        # Check if there are any records for the given truck and user
        if total_km['total_km'] is None:
            return Response({"error": "No records found for this truck and user"}, status=status.HTTP_204_NO_CONTENT)

        # Return the total kilometers and fuel consumption as a response
        return Response({
            "registration_plate": registration_plate,
            "username": req_username,
            "total_km": total_km['total_km'],
            "fuel_used": total_km['total_fuel']
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    # learning how to use F object
@api_view(["GET"])
def increase_km(request):
    try:
        registration_plate = request.query_params.get('registration_plate')
        req_km = request.query_params.get('km')
        
        if not registration_plate or not req_km:
            return Response({"error": "Registration plate or km not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Convert req_km to integer, since it's coming from query params as a string
        req_km = int(req_km)
        
        # Perform the update with F() expressions for arithmetic
        increase_km = WorkingDayModel.objects.filter(
            Q(truck_used__exact=registration_plate) &
            Q(km_driven__lte=req_km)
        ).update(km_driven=F("km_driven") + 1000)
        
        if increase_km == 0:
            return Response({"error": "No data matches the searching criteria"}, status=status.HTTP_204_NO_CONTENT)
        
        # Retrieve the updated records and serialize them
        updated_data = WorkingDayModel.objects.filter(
            Q(truck_used__exact=registration_plate) &
            Q(km_driven__lte=req_km + 1000)
        )
        serializer = SerializerWorkingDayModel(updated_data, many=True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
