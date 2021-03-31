from rest_framework import serializers

class ResourceAllocateSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=50, required=True)
