from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

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
