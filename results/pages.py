from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import string    

class questions1(Page):
    form_model = 'player'
    form_fields = ['p_risk','p_time','p_you','p_others','p_altruism','p_reciprocity','p_inequality','p_beliefs','p_math','p_time2','p_pension'] 

#    def before_next_page(self):
#        self.player.payoff_complete()

class questions2(Page):
    form_model = 'player'
    form_fields = ['p_women1','p_women2','p_women3','p_women4','p_women5','p_women6','p_women7','p_women8','p_pension2'] 

class questions3(Page):
    form_model = 'player'
    form_fields = ['p_sex', 'p_age', 'p_married', 'p_job', 'p_educ', 'p_educ1', 'p_ocupation', 'p_inc','p_health', 'p_pc','p_daughter','p_son','p_sister','p_brother','p_parents','p_parents_married','p_mother_age','p_father_age'] 

class thanks(Page):
    def vars_for_template(self): 
        return {
            "identificador" : self.participant.vars['identificador'],
            "payoff_total" : "$"+format(int(str(self.participant.vars['payoff_total']).split(",")[0]),',d'),
            "payoff_complete" : "$"+format(int(str(self.participant.vars['payoff_complete']+(self.participant.vars["icl_pago"]*100)).split(",")[0]),',d'),
            "round_payoff" : self.participant.vars['round_payoff']-1
        }
        
page_sequence = [questions1,questions2, questions3, thanks]
