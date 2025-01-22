from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello from API v1!'})
