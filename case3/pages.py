from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class p9(Page):
    form_model = 'player'
    form_fields = ['p9','p9_1','p9_2']

class p10(Page):
    form_model = 'player'
    form_fields = ['p10']
    def vars_for_template(self): 
        return {
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }

class p11(Page):
    form_model = 'player'
    form_fields = ['p11']
    def vars_for_template(self): 
        return {
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }

class p12(Page):
    timeout_seconds = 2
    form_model = 'player'
    form_fields = ['p12']
    def vars_for_template(self): 
        return {
            'p11' : self.player.p11,
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }
page_sequence = [p9, p10, p11, p12]
