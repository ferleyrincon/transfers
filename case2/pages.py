from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class case2(Page):
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }


class p4(Page):
    form_model = 'player'
    form_fields = ['p4']

    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p5(Page):
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p6(Page):
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p7(Page):
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class case3(Page):
    def vars_for_template(self): 
        return {
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }
page_sequence = [case2, p4, p5, p6, p7, case3]
