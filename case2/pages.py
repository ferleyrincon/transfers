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
    form_fields = ['p4','check_slider_p4']

    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p5(Page):
    form_model = 'player'
    form_fields = ['p5','check_slider_p5']
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p6(Page):
    form_model = 'player'
    form_fields = ['p6','check_slider_p6']
    def vars_for_template(self): 
        return {
            'daniela' : self.participant.vars['daniela'],
            'manuela' : self.participant.vars['manuela']
        }

class p7(Page):
    form_model = 'player'
    form_fields = ['p7_1','check_slider_p7_1','p7_2']
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

class p8(Page):
    form_model = 'player'
    form_fields = ['p8','p8_1','p8_2']

class p9(Page):
    form_model = 'player'
    form_fields = ['p9','check_slider_p9']
    def vars_for_template(self): 
        return {
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }

class p10(Page):
    form_model = 'player'
    form_fields = ['p10_1','p10_2']
    def vars_for_template(self): 
        return {
            'julia' : self.participant.vars['julia'],
            'luisa' : self.participant.vars['luisa']
        }
page_sequence = [case2, p4, p5, p6, p7, case3, p8, p9, p10]
