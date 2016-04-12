from api.models import Game
from rest_framework import serializers


class GameSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = Game
        fields = ('code',
                  'start_date',
                  'round',
                  'phase',
                  'num_players',
                  'max_num_players',
                  'round_start_date',
                  'phase_start_date',
                  'max_draw_time',
                  'max_write_time',
                  'players')