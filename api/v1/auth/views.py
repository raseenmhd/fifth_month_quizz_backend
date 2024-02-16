import requests 
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User as AuthUser
from users.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']
    
    if not AuthUser.objects.filter(username=username,).exists():
        user = AuthUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name= username,
        )
        User.objects.create(
            user=user,
            username=username,
            email=email,
            password=password,
        )
        headers = {
            'Content-Type': 'application/json',
        }
        
        data={
            "username":username,
            "password":password,
        }
        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
            
        host = request.get_host()

        url = protocol + host + "/api/v1/auth/token/"

        response = requests.post(url, headers=headers, data=json.dumps(data))
          
        if response.status_code == 200:   
            response_data = {
                "status_code": 6000,
                "data" : response.json(),
                "message": "User Created Successfully"
            }
            
        else:
            response_data = {
                "status_code": 6001,
                "message": "encountered error while creating user"
            }
    else:
        response_data = {
            "status_code": 6001,
            "message": "Sorry, the account already exists",
        }
        
    return Response(response_data)
