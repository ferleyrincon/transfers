from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class consent(Page):
    form_model = 'player'
    form_fields = ['p1_2','p1_2','p1_3','p1_4','p1_5','p1_6','p1_7','p1_8','p1_9','p1_10']

    def is_displayed(self):
        return self.round_number == 1

class welcome(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1

class case1(Page):
    def vars_for_template(self): 
        return {
            "camila" : Constants.camila
        }


class case2(Page):
    def vars_for_template(self): 
        return {
            "daniela" : Constants.daniela,
            "manuela" : Constants.manuela
        }

class case3(Page):
    def vars_for_template(self): 
        return {
            "julia" : Constants.julia,
            "luisa" : Constants.luisa
        }

page_sequence = [consent, welcome, case1, case2, case3]
