from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.id, self.name, self.type)

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
