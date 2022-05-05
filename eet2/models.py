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
                p.participant.vars['icl_payoffA'] = [c(Constants.payoffA)]
                p.participant.vars['icl_switching_row_2'] = 2 ** Constants.num_choices


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

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_payoffA(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.payoffA = self.participant.vars['icl_payoffA'][self.round_number - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_payoffA'].append(
                    c(self.participant.vars['icl_payoffA'][self.round_number - 1]
                    + Constants.delta_2 / 2 ** (self.round_number - 1))
                )
            elif self.choice == 'B':
                self.participant.vars['icl_payoffA'].append(
                    c(self.participant.vars['icl_payoffA'][self.round_number - 1]
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
            completed_choices = len(self.participant.vars['icl_payoffA'])
            self.participant.vars['icl_choice_to_pay'] = random.randint(1,completed_choices)
            choice_to_pay = self.participant.vars['icl_choice_to_pay']

            # random draw to determine whether to pay the "sender (1)" or "receiver (2)" decision
            # --------------------------------------------------------------------------------------------------------
            #self.in_round(choice_to_pay).random_draw = random.randint(1, 100)
            self.participant.vars['sender'] = random.randint(1,2)
            sender = self.participant.vars['sender']

            # determine whether the Option A or Option B is relevant for payment
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).payoff_relevant = random.choice(['A','B']) \
                if self.in_round(choice_to_pay).choice == 'I' \
                else self.in_round(choice_to_pay).choice

            # set player's payoff
            # --------------------------------------------------------------------------------------------------------
            if self.in_round(choice_to_pay).payoff_relevant == 'A':
                self.in_round(choice_to_pay).payoff_s = self.participant.vars['icl_payoffA'][choice_to_pay - 1]
                if choice_to_pay < 4 : 
                    self.in_round(choice_to_pay).payoff_r = 65000
                else:
                    self.in_round(choice_to_pay).payoff_r = 35000
            elif self.in_round(choice_to_pay).payoff_relevant == 'B':
                self.in_round(choice_to_pay).payoff_s = Constants.optionB
                self.in_round(choice_to_pay).payoff_r = Constants.optionB

            # set payoff as global variable
            # --------------------------------------------------------------------------------------------------------
            self.participant.vars['icl_payoff'] = self.in_round(choice_to_pay).payoff

            # implied switching row
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).switching_row = self.participant.vars['icl_switching_row_2']