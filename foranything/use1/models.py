from django.db import models

class InternDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'intern_details'

    def __str__(self):
        return self.name
