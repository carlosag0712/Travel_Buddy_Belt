from __future__ import unicode_literals
from ..log_reg.models import *
from django.db import models
from datetime import date, datetime
from dateutil.parser import parse as parse_date

class TripManager(models.Manager):
    def validate_trip(self, postData):
        errors = {}

        if len(postData['destination'])<1:
            errors['destination'] = 'Please enter a destination'

        if len(postData['description'])<1:
            errors['description'] = 'Please enter a description'

        # try:
        #     postData['date_travel_from']
        #     postData['date_travel_to']
        # except KeyError:
        #     errors['nodate'] = 'Please enter a date'
        #

        # if len(postData['date_travel_from'])<1:
        #     errors['nodate'] = 'Please enter a date'
        #
        # if len(postData['date_travel_to'])<1:
        #     errors['nodate'] = 'Please enter a date'

        datefrom_form = postData['date_travel_from']
        datefrom = parse_date(datefrom_form)

        if datefrom.date() < date.today():
            errors['datefrom'] = 'That ship has sailed! Please pick a future date'

        dateto_form = postData['date_travel_to']
        dateto = parse_date(dateto_form)

        if dateto.date() < date.today() :
            errors['dateto'] = 'Invalid date'

        if dateto < datefrom:
            errors['date'] = 'You kinda need to go before you are back!'

        return errors


class travel(models.Model):
    destination = models.TextField(max_length=100)
    description = models.TextField(max_length=150)
    date_travel_from = models.DateField()
    date_travel_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_planner = models.ForeignKey(users, related_name='planner')
    user_joining = models.ManyToManyField(users, related_name='tag_along')
    objects = TripManager()

# Create your models here.
