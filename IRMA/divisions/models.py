from django.db import models


class BUnit(models.Model):
    structure = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.structure, self.department, self.position)

    class Meta:
        verbose_name = 'Рабочее подразделение'
        verbose_name_plural = 'Рабочие подразделения'
