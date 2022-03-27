from enum import unique
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="O numero de telefone deve estar no formato: '999999999'. Ate 15 digitos sao permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(blank=True, null=True)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

