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
    pass


class case2(WaitPage):
    pass


class case3(Page):
    pass


page_sequence = [consent, welcome, case1, case2, case3]
