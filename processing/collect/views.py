from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collect.models import Mission
from collect.serializers import MissionSerializer


@api_view(['GET', 'POST'])
def mission_list(request):
    # collect a new mission to be processed
    if request.method == 'POST':
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        missions = Mission.objects.all()
        serializer = MissionSerializer(missions, many=True)
        return Response(serializer.data)
