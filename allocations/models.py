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

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
   pass

class Player(BasePlayer):
    #pago = models.CurrencyField()
    #payoff_complete  = models.CurrencyField()
    camila = models.BooleanField(blank=True) #Hija 1
    daniela= models.BooleanField(blank=True) #Hermana 2.1
    manuela= models.BooleanField(blank=True) #Hermana 2.2
    julia=   models.BooleanField(blank=True) #Hermana 3.1
    luisa=   models.BooleanField(blank=True) #Hermana 3.2
    
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')
    
    case2_7 = models.IntegerField(blank=9, widget=widgets.RadioSelectHorizontal, 
                                 label="Escriba si se le ocurre una solución adicional:", 
                                 choices=[  [0, "0%"],
                                            [0, "30%"],
                                            [1, "50%"],
                                            [0, "60%"],
                                            [0, "90%"],
                                            [0, "100%"]])
    p_random2 = models.IntegerField(blank=9,widget=widgets.RadioSelectHorizontal, 
                                 label="2. Usted hace 6 secuencias, y los otros participantes también hacen 6 secuencias cada uno. Su probabilidad de tener el Contrato A en la siguiente ronda es:", 
                                 choices=[  [0, "0"],
                                            [0, "30%"],
                                            [1, "50%"],
                                            [0, "60%"],
                                            [0, "90%"],
                                            [0, "100%"]])
    p_perfect1 = models.IntegerField(blank=9,widget=widgets.RadioSelectHorizontal, 
                                 label="1. Usted hace 6 secuencias, y el otro participante hace 4 secuencias. Su probabilidad de tener el Contrato A en la siguiente ronda es:", 
                                 choices=[  [0, "0%"],
                                            [0, "30%"],
                                            [0, "50%"],
                                            [0, "60%"],
                                            [0, "90%"],
                                            [1, "100%"]])
    p_perfect2 = models.IntegerField(blank=9,widget=widgets.RadioSelectHorizontal, 
                                 label="2. Usted hace 6 secuencias, y el otro participante también hace 6 secuencias. Su probabilidad de tener el Contrato A la siguiente ronda es:", 
                                 choices=[  [0, "0%"],
                                            [0, "30%"],
                                            [1, "50%"],
                                            [0, "60%"],
                                            [0, "90%"],
                                            [0, "100%"]])
    p_noisy1= models.IntegerField(blank=9,widget=widgets.RadioSelectHorizontal, 
                                 label="1. Usted hace 6 secuencias, y el otro participante hace 4 secuencias. Su probabilidad de tener el Contrato A en la siguiente ronda es:", 
                                 choices=[  [0, "0%"],
                                            [0, "30%"],
                                            [0, "50%"],
                                            [1, "60%"],
                                            [0, "90%"],
                                            [0, "100%"]])
    p_noisy2= models.IntegerField(blank=9,widget=widgets.RadioSelectHorizontal, 
                                 label="2. Usted hace 6 secuencias, y el otro participante también hace 6 secuencias. Su probabilidad de tener el Contrato A en la siguiente ronda es:", 
                                 choices=[  [0, "0%"],
                                            [0, "30%"],
                                            [1, "50%"],
                                            [0, "60%"],
                                            [0, "90%"],
                                            [0, "100%"]])

    #Esta función define el pago final
    def set_payoff(self):
        if (self.round_number==Constants.num_rounds):
            ronda = self.subsession.round_payoff
            payoff_rounds = []
            for j in self.in_all_rounds():
                payoff_rounds.append(j.payoff_round)
            self.pago= payoff_rounds[ronda- 1]
            self.participant.vars['identificador'] = self.in_round(1).identificador
            self.participant.vars['payoff_total'] = self.pago
            self.participant.vars['round_payoff'] = self.subsession.round_payoff
        else:
            self.pago= 0
 #           j.pago = j.pago_ronda.in_all_rounds()[ronda - 1]
        
    def set_likelihood_contract_A(self):
        if (self.round_number!=1):
            if self.subsession.discrimination == 0:
                self.likelihood_contract_A = 0.5
            else:                     
                if (self.contract_A == True and self.position_contract == 1):
                        self.likelihood_contract_A = 1
                elif (self.contract_A == False and self.position_contract == 2):
                        self.likelihood_contract_A = 0
                else:
                    if self.subsession.discrimination == 1:#(perfect)
                        if (self.tasks > self.group.get_tasks_tournament()/2):
                            self.likelihood_contract_A = 1
                        elif (self.tasks == self.group.get_tasks_tournament()/2):
                            self.likelihood_contract_A = 0.5
                        else:
                            self.likelihood_contract_A = 0
                    else: #subsession.discrimination == 2 (noisy)
                        if self.group.get_tasks_tournament() == 0:
                            self.likelihood_contract_A = 0.5
                        else:
                            self.likelihood_contract_A = self.tasks / self.group.get_tasks_tournament()

    def set_position_group(self):
        rank = json.loads(self.group.rank)
        self.position_group = list(rank.keys()).index('j' + str(self.id_in_group)) + 1
    
    def set_position_contract(self):
        rankA = json.loads(self.group.rankA)
        rankB = json.loads(self.group.rankB)
        if self.contract_A:
            self.position_contract = list(rankA).index('j' + str(self.id_in_group)) + 1
            self.position_ranking = list(rankA).index('j' + str(self.id_in_group)) + 1
        else:
            self.position_contract = list(rankB).index('j' + str(self.id_in_group)) + 1
            self.position_ranking = list(rankB).index('j' + str(self.id_in_group)) + 3

    def set_contract_A_tournament(self):
            winner = self.group.winner_contract_A
            if (self.contract_A == True and self.position_contract == 1) or (self.contract_A == False and self.position_contract == 2):
                self.contract_A_tournament = self.contract_A
                if self.position_contract == 1:
                    self.position_contract_tournament = 1
                else:
                    self.position_contract_tournament = 2
            else:
                if self.id_in_group == int(winner):
                    self.contract_A_tournament = True
                    self.position_contract_tournament = 2
                else:
                    self.contract_A_tournament = False
                    self.position_contract_tournament = 1

    def set_payoff_round(self):
        if (self.contract_A):
            self.payoff_round= Constants.payoff_A * self.tasks
        else:
            self.payoff_round = Constants.payoff_B * self.tasks

    def set_payoff_complete(self):
        if (self.round_number==Constants.num_rounds):
            self.payoff_complete= self.pago + 10000
            self.participant.vars['payoff_complete']= self.pago + 10000
        return self.participant.vars['payoff_complete']