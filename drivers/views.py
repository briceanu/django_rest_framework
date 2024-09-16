from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from drivers.serializers import DriverSerializer 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# Create your views here.






# view for the users to sign up
@api_view(['POST'])
def signup(request):
    try:
        serializer = DriverSerializer(data=request.data) 
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"data saved"},status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    






@api_view(['POST'])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error":"email or password not provided"},status=status.HTTP_400_BAD_REQUEST)
        try:
            authenticate_user = authenticate(username=username,password=password)
            if  authenticate_user is None:
                return Response({"error":"invalid credentials"},status=status.HTTP_403_FORBIDDEN)
            refresh_token = RefreshToken.for_user(authenticate_user)
            access_token = refresh_token.access_token
            return Response({
                "access":str(access_token),
                "refresh":str(refresh_token)},status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"error":str(e)},status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)






@api_view(["GET"])
def get_drivers(request):
    trucks = User.objects.all()
    serializer = DriverSerializer(trucks,many=True)
    return Response({"sucess":serializer.data},status=status.HTTP_200_OK)