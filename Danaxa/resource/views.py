from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

class ResourceManager(APIView):
    serializer_class = serializers.ResourceAllocateSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        return Response({'detail': 'succeed'})