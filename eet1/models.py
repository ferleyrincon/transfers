from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from eet1.config import *
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
                p.participant.vars['icl_payoffA_1'] = [c(Constants.payoffA)]
                p.participant.vars['icl_switching_row_1'] = 2 ** Constants.num_choices
                p.participant.vars['eet_round_to_pay'] = random.randint(1,6)

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
    payoff_relevant = models.StringField()
    payoffA = models.CurrencyField()
    choice = models.StringField()
    switching_row_1 = models.IntegerField()

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_choice_eet(self):
        if (self.round_number==self.participant.vars['eet_round_to_pay']):
            self.participant.vars['eet_choice']= self.choice     

    def set_payoffA_eet(self):
        if (self.round_number==self.participant.vars['eet_round_to_pay']):
            self.participant.vars['eet_payoffA']= self.payoffA 

    def set_payoffA(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.payoffA = self.participant.vars['icl_payoffA_1'][self.round_number - 1]
        
        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_payoffA_1'].append(
                    c(self.participant.vars['icl_payoffA_1'][self.round_number - 1]
                    + Constants.delta_1 / 2 ** (self.round_number - 1))
                )
            elif self.choice == 'B':
                self.participant.vars['icl_payoffA_1'].append(
                    c(self.participant.vars['icl_payoffA_1'][self.round_number - 1]
                    - Constants.delta_1 / 2 ** (self.round_number - 1))
                )
            else:
                pass

        # implied switching row
        # --------------------------------------------------------------------------------------------------------
        self.in_round(3).switching_row_1 = self.participant.vars['icl_switching_row_1']

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row_1'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row_1'] /= 2

