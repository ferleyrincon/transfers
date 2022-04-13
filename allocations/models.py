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
    name_in_url = 'allocations'
    players_per_group = None
    num_rounds = 1
    fixed_payoff = c(10000)
    likelihood_pago= 0.1
    likelihood_sender=0.5
    likelihood_receiver=0.5
    age_category= {
    # "contract#" : [paymnet, insurance, bonus relative , alone ]    
        "r1" :  [18 , 34],
        "r2" :  [35 , 56], #57: Edad de pensión mujeres
        "r3" :  [57 , 90],
    # More than 90 years: warning about the possibility of identity theft. 
    }
    camila = random.choice([True, False])
    daniela = random.choice([True, False])
    manuela = random.choice([True, False])
    julia = random.choice([True, False])
    luisa = random.choice([True, False])

class Subsession(BaseSubsession):
    camila = models.BooleanField() #Hija 1
    daniela = models.BooleanField()#Hermana 2.1
    manuela = models.BooleanField()#Hermana 2.2
    julia = models.BooleanField()  #Hermana 3.1
    luisa = models.BooleanField()  #Hermana 3.2


    def creating_session(self):
            """Esta función define los valores iniciales para cada ronda
            incluye la subsession y demás clases.
            Este método se ejecuta al comiezo de la sesion tantas veces como
            rondas haya"""
            self.camila = Constants.camila
            self.daniela = Constants.daniela
            self.manuela = Constants.manuela
            self.julia = Constants.julia
            self.luisa = Constants.luisa

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')

    p1_1 =  models.StringField()
    p1_2 =  models.StringField()
    p1_3 =  models.StringField()
    p1_4 =  models.StringField()
    p1_5 =  models.StringField()
    p1_6 =  models.StringField()
    p1_7 =  models.StringField()
    p1_8 =  models.StringField()
    p1_9 =  models.StringField()
    p1_10 =  models.StringField()

    p2_1 =  models.StringField()
    p2_2 =  models.StringField()
    p2_3 =  models.StringField()
    p2_4 =  models.StringField()
    p2_5 =  models.StringField()
    p2_6 =  models.StringField()
    p2_7 =  models.StringField()
    p2_8 =  models.StringField()
    p2_9 =  models.StringField()
    p2_10 =  models.StringField()

    p3_1 =  models.StringField()
    p3_2 =  models.StringField()
    p3_3 =  models.StringField()
    p3_4 =  models.StringField()
    p3_5 =  models.StringField()
    p3_6 =  models.StringField()
    p3_7 =  models.StringField()
    p3_8 =  models.StringField()
    p3_9 =  models.StringField()
    p3_10 =  models.StringField()

    p4 =  models.IntegerField()
    check_slider_p4 =  models.IntegerField()
    p5 =  models.IntegerField()
    check_slider_p5 =  models.IntegerField()
    p6 =  models.IntegerField()
    check_slider_p6 =  models.IntegerField()
    p7_1 =  models.IntegerField()
    check_slider_p7_1 =  models.IntegerField()
    p7_2 =  models.StringField(label='Escriba una solución adicional:')

    p8_1 =  models.StringField()
    p8_2 =  models.StringField()
    p8_3 =  models.StringField()
    p8_4 =  models.StringField()
    p8_5 =  models.StringField()
    p8_6 =  models.StringField()
    p8_7 =  models.StringField()
    p8_8 =  models.StringField()
    p8_9 =  models.StringField()
    p8_10 =  models.StringField()
    p10 =  models.IntegerField()

    p9 = models.IntegerField(
    choices=[
        [1,'A un banco o entidad financiera.'],
        [2,'A una persona diferente a los hijos.'],
        [3,'A los hijos, a un precio menor al que recibirían de alguien que no sea de la familia.'],
        [4,'A los hijos, al mismo precio que recibirían de alguien que no sea de la familia. '],
    ], label="Si los padres deciden vender la casa ¿A quién deberían vendérsela?")

    p9_1 = models.IntegerField(
    choices=[
        [1,'Solicitar un pago único correspondiente al valor total de la casa.'],
        [2,'Solicitar un pago cada mes, de un monto acordado con la entidad financiera, por un número determinado de años.'],
        [3,'Solicitar un pago cada mes, hasta que fallezcan, de un monto acordado con la entidad financiera. Este monto es más bajo que si lo escogen por un número determinado de años.'],
    ], label="Si los padres deciden vender la casa a una entidad financiera, ¿cuál de estas opciones deberían escoger?")

    p9_2 = models.IntegerField(
    choices=[
        [1,'Solicitar un pago único correspondiente al valor total de la casa.'],
        [2,'Solicitar un pago cada mes, de un monto acordado con los hijos, por un número determinado de años.'],
        [3,'Solicitar un pago cada mes, hasta que fallezcan, de un monto acordado con los hijos. Este monto es más bajo que si lo escogen por un número determinado de años.'],
    ], label="Si los padres deciden vender la casa a los hijos, ¿cuál de estas opciones deberían escoger?")

    p11_1 = models.IntegerField(
    choices=[
        [1,'Solicitar un pago único correspondiente al valor total de la casa.'],
        [2,'Solicitar un pago cada mes, de un monto acordado con los hijos, por un número determinado de años.'],
        [3,'Solicitar un pago cada mes, hasta que fallezcan, de un monto acordado con los hijos. Este monto es más bajo que si lo escogen por un número determinado de años.'],
    ], label="¿Qué cree que debería hacerse en ese caso?")

    p11_2 =  models.StringField(label='Escriba una solución adicional:')




