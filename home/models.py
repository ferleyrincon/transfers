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
    name_in_url = 'home'
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

class Subsession(BaseSubsession):
    def creating_session(self):
        for j in self.get_players():
            j.get_camila()
            j.get_daniela()
            j.get_manuela()
            j.get_julia()
            j.get_luisa()
            j.get_old()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')

    camila = models.BooleanField() #Hija 1
    daniela = models.BooleanField()#Hermana 2.1
    manuela = models.BooleanField()#Hermana 2.2
    julia = models.BooleanField()  #Hermana 3.1
    luisa = models.BooleanField()  #Hermana 3.2
    old = models.BooleanField()  #Hermana 3.2


    def get_camila(self):
        self.camila =random.choice([True, False])
        self.participant.vars['camila'] =self.camila
        return self.camila

    def get_daniela(self):
        self.daniela =random.choice([True, False])
        self.participant.vars['daniela'] =self.daniela
        return self.daniela

    def get_manuela(self):
        self.manuela =random.choice([True, False])
        self.participant.vars['manuela'] =self.manuela
        return self.manuela
    
    def get_julia(self):
        self.julia =random.choice([True, False])
        self.participant.vars['julia'] =self.julia
        return self.julia

    def get_luisa(self):
        self.luisa =random.choice([True, False])
        self.participant.vars['luisa'] =self.luisa
        return self.luisa

    def get_old(self):
        self.old =random.choice([True, False])
        self.participant.vars['old'] =self.old
        return self.old