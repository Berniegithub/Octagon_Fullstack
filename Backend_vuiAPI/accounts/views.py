from django.urls import reverse 
from django.http import Http404 
from rest_framework import generics
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from . models import Login, Register, Profile
from . serializers import UserSerializer,RegisterSerializer, ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login



class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
      phone_number = request.data.get('Phone_number')
      password = request.data.get('password')

      if not phone_number or not password:
          return Response({'error': 'Phone number and Password are required.'}, status=status.HTTP_400_BAD_REQUEST)
      
      #Authenticate the user 
      user = authenticate(request, phone_number=phone_number, password=password)

      if user is not None:
          login(request, user)
          serializer = self.serializer_class(user)
          return Response({'message': 'Logged in successfully', 'user_data': serializer.data}, status=status.HTTP_200_OK)
      else:
          return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    



class UserProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def get_object(self):
        pk  = self.kwargs.get(self.lookup_url_kwarg)
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404('Profile does not exist for this user. ')
    

    
class RegisterView(generics.CreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
           user_profile_url = reverse('user-profile', kwargs={'pk': user.pk})
           return Response({"message": "User registered successfully", "user_profile_url": user_profile_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)