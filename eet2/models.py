from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from eet2.config import *
import random


author = 'Felix Holzmeister'

doc = """
Staircase risk elicitation task as proposed by Falk et al. (2016), Working Paper.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs and implied switching row in first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['icl_payoffA_2'] = [c(Constants.payoffA)]
                p.participant.vars['icl_switching_row_2'] = 2 ** Constants.num_choices

    def set_eet(self):
        for j in self.get_players():
            j.set_choice_eet()
            j.set_payoffA_eet()

# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass



# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ----------------------------------------------------------------------------------------------------------------
    random_draw = models.IntegerField()
    sender= models.IntegerField()
    payoff_relevant = models.StringField()
    payoffA = models.CurrencyField()
    payoff_s = models.CurrencyField()
    payoff_r = models.CurrencyField()
    choice = models.StringField()
    choice_to_pay = models.IntegerField()
    switching_row = models.IntegerField()
    situation = models.IntegerField()


    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_choice_eet(self):
        self.situation=self.round_number+3
        if (self.situation==self.participant.vars['eet_round_to_pay']):
            self.participant.vars['eet_choice']= self.choice
        

    def set_payoffA_eet(self):
        self.situation=self.round_number+3
        if (self.situation==self.participant.vars['eet_round_to_pay']):
            self.participant.vars['eet_payoffA']= self.payoffA 


    def set_payoffA(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.payoffA = self.participant.vars['icl_payoffA_2'][self.round_number - 1]


        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_payoffA_2'].append(
                    c(self.participant.vars['icl_payoffA_2'][self.round_number - 1]
                    + Constants.delta_2 / 2 ** (self.round_number - 1))
                )
            elif self.choice == 'B':
                self.participant.vars['icl_payoffA_2'].append(
                    c(self.participant.vars['icl_payoffA_2'][self.round_number - 1]
                    - Constants.delta_2 / 2 ** (self.round_number - 1))
                )
            else:
                pass

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row_2'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row_2'] /= 2

    # set payoffs
    # ----------------------------------------------------------------------------------------------------------------
    def set_payoffs(self):

        current_round = self.subsession.round_number
        current_choice = self.in_round(current_round).choice

        # set payoff if all choices have been completed or if "indifferent" was chosen
        # ------------------------------------------------------------------------------------------------------------
        if current_round == Constants.num_rounds or current_choice == 'I':

            # randomly determine which choice to pay
            # --------------------------------------------------------------------------------------------------------
            completed_choices = len(self.participant.vars['icl_payoffA_2'])
            self.participant.vars['icl_choice_to_pay'] = random.randint(1,completed_choices)
            choice_to_pay = self.participant.vars['icl_choice_to_pay']

            # determine whether the Option A or Option B is relevant for payment
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).payoff_relevant = random.choice(['A','B']) \
                if self.in_round(choice_to_pay).choice == 'I' \
                else self.in_round(choice_to_pay).choice

            # set player's payoff
            # --------------------------------------------------------------------------------------------------------
            if self.participant.vars['eet_choice'] == 'A':
                self.payoff_s = self.participant.vars['eet_payoffA']
                if self.participant.vars['eet_round_to_pay'] < 4 : 
                    self.payoff_r = 65000
                else:
                    self.payoff_r = 35000
            elif self.participant.vars['eet_choice'] =='B':
                self.payoff_s = Constants.optionB
                self.payoff_r = Constants.optionB
            self.participant.vars['pagototal']=self.payoff_s+15000

            # set payoff as global variable
            # --------------------------------------------------------------------------------------------------------
            #self.participant.vars['icl_payoff'] = self.in_round(choice_to_pay).payoff

            # implied switching row
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).switching_row = self.participant.vars['icl_switching_row_2']