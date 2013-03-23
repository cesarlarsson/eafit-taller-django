from django.db import models


class Encuesta(models.Model):
    pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('date published')

    def __unicode__(self):
        return self.pregunta

    def was_published_recently(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    respuesta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
        return self.respuesta
