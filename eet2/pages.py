from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        #'p_hi': "{0:.0f}".format(Constants.probability) + "%",
        #'p_lo': "{0:.0f}".format(100 - Constants.probability) + "%",
        'optionB':"$ "+format(int(str(Constants.optionB).split(",")[0]), ',d'),
        'otherA_2': "$ "+format(int(str(Constants.otherA_2).split(",")[0]), ',d')        
    }
# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # only display if previous choice was not "indifferent"
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        previous_choices = [p.choice for p in self.player.in_previous_rounds()]
        return 'I' not in previous_choices

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'page':        page+3,
            'total':       total,
            'progress':    progress,
            'payoffA': "$ "+format(int(str((self.participant.vars['icl_payoffA_2'][page - 1])).split(",")[0]), ',d')
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_payoffA()
        self.player.update_switching_row()
        self.player.set_payoffs()
        self.subsession.set_eet()


# ******************************************************************************************************************** #
# *** PAGE RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):
    form_model = 'player'
    form_fields = ['payoff_total', 'payoff_resignation', 'payoff_otherPlayer']

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        choice_to_pay = self.participant.vars['eet_round_to_pay']
        payoff_relevant = self.participant.vars['eet_choice']
        payoffA = self.participant.vars['eet_payoffA']

        return {
            #"old" : self.participant.vars['old'],
            'payoffA':          "$ "+format(int(str(self.participant.vars['eet_payoffA']).split(",")[0]), ',d'),
            'choice_to_pay':    self.participant.vars['eet_round_to_pay'],
            'option_to_pay':    self.participant.vars['eet_choice'],
            'payoff_s':         "$ "+format(int(str(self.player.payoff_s).split(",")[0]), ',d'),
            'payoff_r':         "$ "+format(int(str(self.player.payoff_r).split(",")[0]), ',d'),
            'payoff_total':     "$ "+format(int(str(self.player.payoff_r+self.player.payoff_s).split(",")[0]), ',d'),
            'payoff_total_int': int(str(self.player.payoff_r+self.player.payoff_s).split(",")[0])
        }

# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)

if Constants.results:
    page_sequence.append(Results)
