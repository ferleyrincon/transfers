from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from parents.config import *
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
                p.participant.vars['icl_sure_payoffs_p1'] = [c(Constants.sure_payoff)]
                p.participant.vars['icl_switching_row_p1'] = 2 ** Constants.num_choices


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
    sure_payoff = models.CurrencyField()
    choice = models.StringField()
    switching_row_p1 = models.IntegerField()

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_sure_payoffs(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.sure_payoff = self.participant.vars['icl_sure_payoffs_p1'][self.round_number - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_sure_payoffs_p1'].append(
                    c(self.participant.vars['icl_sure_payoffs_p1'][self.round_number - 1]
                    + Constants.delta / 2 ** (self.round_number - 1))
                )
            elif self.choice == 'B':
                self.participant.vars['icl_sure_payoffs_p1'].append(
                    c(self.participant.vars['icl_sure_payoffs_p1'][self.round_number - 1]
                    - Constants.delta / 2 ** (self.round_number - 1))
                )
            else:
                pass

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row_p1'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row_p1'] /= 2

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
            completed_choices = len(self.participant.vars['icl_sure_payoffs_p1'])
            self.participant.vars['icl_choice_to_pay_p1'] = random.randint(1, completed_choices)
            choice_to_pay = self.participant.vars['icl_choice_to_pay_p1']

            # determine whether the lottery or sure payoff is relevant for payment
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).payoff_relevant = random.choice(['A','B']) \
                if self.in_round(choice_to_pay).choice == 'I' \
                else self.in_round(choice_to_pay).choice

            # set player's payoff
            # --------------------------------------------------------------------------------------------------------
            if self.in_round(choice_to_pay).payoff_relevant == 'A':
                self.in_round(choice_to_pay).payoff = Constants.hours
            elif self.in_round(choice_to_pay).payoff_relevant == 'B':
                self.in_round(choice_to_pay).payoff = self.participant.vars['icl_sure_payoffs_p1'][choice_to_pay - 1]

            # set payoff as global variable
            # --------------------------------------------------------------------------------------------------------
            self.participant.vars['icl_payoff'] = self.in_round(choice_to_pay).payoff

            # implied switching row
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).switching_row_p1 = self.participant.vars['icl_switching_row_p1']
