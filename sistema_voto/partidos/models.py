from django.db import models
from django.utils.text import slugify
from stdimage import StdImageField
from datetime import datetime

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

def favicon_dir(instance, filename):
    dt = datetime.now()
    extesion = str(filename).split('.')[:-1]
    filename = str(dt.strftime('%D%Y%M_IMAGE'))+ str(extesion) 

    return 'partidos/%D/%Y/{}' .format(filename)
class Partido(models.Model):
    name = models.CharField(max_length=50)
    name_url = models.CharField(max_length=50, editable=False)

    slogan = models.TextField()

    favicon = StdImageField(upload_to=favicon_dir, variations={
        'large': (3840, 2160, True), 'thumbnail': (400, 300, True)
    })

    qtd_votos = models.ManyToManyField(User, related_name='qtd_votos', blank=True, default=None)

    def __str__(self):
        return 'partido_{}' .format(self.pk)
    
    def save(self, *args, **kwargs):
        self.name_url = slugify(self.name)

        return super().save(*args, **kwargs)


CHOICES_VOTOS = [
    ('voto', 'voto'),
    ('unVoto', 'unVoto')
]

class Voto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

    value = models.CharField(max_length=7, choices=CHOICES_VOTOS, default='unVoto')

    def __str__(self):
        return 'voto_{}' .format(self.pk)