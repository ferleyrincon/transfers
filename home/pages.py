from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class device(Page):
    def is_displayed(self):
        return self.round_number == 1

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
    
    def before_next_page(self):
        self.subsession.set_id_players()

class case1(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            "camila" : self.participant.vars['camila']
        }

page_sequence = [device, consent, welcome,case1]
