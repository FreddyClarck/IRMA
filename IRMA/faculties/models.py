from django.db import models


class TUnit(models.Model):
    faculty = models.CharField(max_length=100)
    chair = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.faculty, self.chair, self.position)

    class Meta:
        verbose_name = 'Учебное подразделение'
        verbose_name_plural = 'Учебные подразделения'
