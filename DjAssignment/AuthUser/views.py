from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserCreateSerializer,UserDetailSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions




class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Username and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        user_data = UserDetailSerializer(user).data  # serialize user info

        return Response(
            data={
                "token": str(refresh.access_token),
                "user": user_data
            },
            status=status.HTTP_200_OK
        )

class RegisterUser(APIView):
    # permission_classes = [IsAuthenticated]  
    permission_classes = [permissions.AllowAny] 
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save() 
            return Response({"data":serializer.data ,"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
