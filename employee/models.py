from django.db import models

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Должность'

class InformationEmployee(models.Model):
    full_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employment_day = models.DateField()
    salary = models.IntegerField(blank=True, null=True)
    chief = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return '{}'.format(self.full_name)

    class Meta:
        verbose_name = 'Информация о каждом сотруднике'
        verbose_name_plural = 'Информация о  сотрудниках'










