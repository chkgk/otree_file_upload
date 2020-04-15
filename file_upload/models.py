from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

# for file / image upload
from django.db import models as django_models

author = 'Christian König gen. Kersting'

doc = """
Image and File Upload Demo for oTree
"""


class Constants(BaseConstants):
    name_in_url = 'file_upload'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    image = django_models.ImageField(upload_to="images")
    file = django_models.FileField(upload_to="files")
