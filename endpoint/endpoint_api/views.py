from rest_framework.views import APIView
import jwt
from django.http import JsonResponse

# Create your views here.
class EndpointApiView(APIView):
    def get(self, request):
        data = {
            'login': 'kamil',
            'password':'1234',
        }

        return JsonResponse(data)
    
    def post(self, request):
        data = {
            'login': request.data.get('login'), 
            'password': request.data.get('password')
        }


        jwt_token = jwt.encode({'token': "siema"}, "secret", "HS256")

        return JsonResponse(data, safe=False)
