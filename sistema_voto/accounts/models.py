from django.db import models
from django.contrib import auth
from django.utils.text import slugify
import re
# Create your models here.

# Function validator Bi number
def bi_validator(value):
    padrao = re.compile(r'00[0-9]+[A-Z]+[A-Z]+[0-9]*')
    if not(padrao.search(value)):
        return 'Número do Bilhete de Identidade invalido'

class User(auth.models.User, auth.PermissionDenied):

    def __str__(self):
        return 'user_{}' .format(self.pk)

class UserOthersInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bi = models.CharField(max_length=14, validators=[bi_validator])

    def __str__(self):
        return 'user_{}' .format(self.user.pk)