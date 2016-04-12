from api.models import Game
from api.serializers import GameSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = Game.objects.all().order_by('-start_date')
        serializer = GameSerializer

        return Response(serializer.data)

    def retrieve(self, request, key=None):
        return True

    def create(self, request):
        return True
