from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
import random
import json

from otree.models import subsession

author = 'Cesar Mantilla & Ferley Rincon'

doc = """
Adult children gender and what they should transfer to their parents: a survey experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'case2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p4 =  models.IntegerField()
    check_slider_p4 =  models.IntegerField()

    p5 =  models.IntegerField()
    check_slider_p5 =  models.IntegerField()

    p6 =  models.IntegerField()
    check_slider_p6 =  models.IntegerField()

    p7_1 =  models.IntegerField()
    check_slider_p7_1 =  models.IntegerField()
    p7_2 =  models.StringField()

    p8 = models.IntegerField()
    p8_1 = models.IntegerField()
    p8_2 = models.IntegerField()

    p9=  models.IntegerField()
    check_slider_p9 =  models.IntegerField()

    p10_1 = models.IntegerField()

    p10_2 =  models.StringField()

    p11_1 = models.IntegerField()
    p11_2 =  models.StringField()