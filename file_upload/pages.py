from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Upload(Page):
    form_model = 'player'
    form_fields = ['image', 'file']

class Display(Page):
    pass

page_sequence = [Upload, Display]
