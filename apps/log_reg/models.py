from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

passCheck = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])\w{8}')

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        try:
            validate_email(postData['reg_email'])
        except ValidationError:
            errors['reg_email'] = "Invalid Email"

        checkEmail = users.objects.filter(email_address=postData["reg_email"])

        if checkEmail:
            errors['reg_email'] = "email already exists"


        if len(postData['reg_first_name']) < 3:
            errors["first_name"] = "names should be more than 2 characters"

        if len(postData['reg_last_name']) < 3:
            errors["last_name"] = "names should be more than 2 characters"

        if not passCheck.match(postData['reg_password']):
            errors['reg_password'] = "Password must be at least 8 characters and must contain at least 1 uppercase and 1 numeric value"

        if postData['reg_password'] != postData['conf_reg_password']:
            errors['reg_password'] = "Passwords do not match"

        return errors

    

class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.TextField(default="NOT_PROVIDED")
    description = models.TextField()
    user_role = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
