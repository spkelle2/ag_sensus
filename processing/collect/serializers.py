from rest_framework import serializers
from collect.models import Mission

class MissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField()
    height = serializers.IntegerField()

    def create(self, validated_data):
        # create and return new Mission, given validated data
        return Mission.objects.create(**validated_data)
