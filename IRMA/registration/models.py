from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.surname, self.name, self.email)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
