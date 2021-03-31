import random

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

class ResourceManager(APIView):
    serializer_class = serializers.ResourceAllocateSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Suppose these are list of current user requests and their weights.
        # In real situation these list are coming from Cache or DB
        users = [f'user{i}' for i in range(5)]
        weights = [round(random.uniform(0, 0.8), 2) for i in range(5)]
        
        # manually assing more weights to user0 (for test purpose)
        weights[0] = 0.99

        choice = random.choices(users, weights)[0]
        if choice == data['user_id']:
            return Response({'accepted': True})
        else:
            return Response({'accepted': False, 'choice': choice, 'users': users, 'weights': weights})
