from __future__ import unicode_literals

from django.db import models

import random

class Game(models.Model):
    ROUNDS = ["setup", "game", "review"]
    PHASES = ["write", "draw"]

    code = models.CharField(max_length=6, default="abcd")
    start_date = models.DateTimeField('date game started')

    round = models.IntegerField(default=ROUNDS[0])
    phase = models.IntegerField(default=PHASES[0])
    round_start_date = models.DateTimeField('date round started')
    phase_start_date = models.DateTimeField('date phase started')

    num_players = models.IntegerField(default=0)

    # options
    max_num_players = models.IntegerField(default=10)
    max_draw_time   = models.IntegerField(default=120)
    max_write_time  = models.IntegerField(default=60)




class Player(models.Model):
    name = models.CharField(max_length=32, default="great player")
    game_id = models.ForeignKey(Game, related_name='players')
    id = models.IntegerField(primary_key=True)

    created_date = models.DateTimeField('date player created')

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)
