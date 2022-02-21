from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class consent(Page):
    def is_displayed(self):
        return self.round_number == 1

class welcome(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1

class case1(Page):
    form_model = 'player'
    form_fields = ['p1_1','p1_2','p1_3','p1_4','p1_5','p1_6','p1_7','p1_8','p1_9','p1_10', 'p2_1','p2_2','p2_3','p2_4','p2_5','p2_6','p2_7','p2_8','p2_9','p2_10','p3_1','p3_2','p3_3','p3_4','p3_5','p3_6','p3_7','p3_8','p3_9','p3_10']

    def vars_for_template(self): 
        return {
            "camila" : Constants.camila
        }


class case2(Page):
    form_model = 'player'
    form_fields = ['p4','p5','p6','p7_1','p7_2']

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
