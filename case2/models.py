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

    p8 = models.IntegerField(
    choices=[
        [1,'A un banco o entidad financiera.'],
        [2,'A una persona diferente a los hijos.'],
        [3,'A los hijos, a un precio menor al que recibirían de alguien que no sea de la familia.'],
        [4,'A los hijos, al mismo precio que recibirían de alguien que no sea de la familia. '],
    ], label="Si los padres deciden vender la casa ¿A quién deberían vendérsela?")

    p8_1 = models.IntegerField(
    choices=[
        [1,'Solicitar un pago único correspondiente al valor total de la casa.'],
        [2,'Solicitar un pago cada mes, de un monto acordado con la entidad financiera, por un número determinado de años.'],
        [3,'Solicitar un pago cada mes, hasta que fallezcan, de un monto acordado con la entidad financiera. Este monto es más bajo que si lo escogen por un número determinado de años.'],
    ], label="Si los padres deciden vender la casa a una entidad financiera, ¿cuál de estas opciones deberían escoger?")

    p8_2 = models.IntegerField(
    choices=[
        [1,'Solicitar un pago único correspondiente al valor total de la casa.'],
        [2,'Solicitar un pago cada mes, de un monto acordado con los hijos, por un número determinado de años.'],
        [3,'Solicitar un pago cada mes, hasta que fallezcan, de un monto acordado con los hijos. Este monto es más bajo que si lo escogen por un número determinado de años.'],
    ], label="Si los padres deciden vender la casa a los hijos, ¿cuál de estas opciones deberían escoger?")

    p9=  models.IntegerField()
    check_slider_p9 =  models.IntegerField()

    p10_1 = models.IntegerField()

    p10_2 =  models.StringField()