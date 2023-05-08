from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


class Organization(models.Model):
    TYPE_CHOICES = (
        ("TI", "TI"),
        ("SAUDE", "Saúde"),
        ("FINANCEIRO", "Financeiro"),
        ("EDUCACAO", "Educação"),
        ("ENERGIA", "Energia"),
        ("ALIMENTICIO", "Alimentício"),
        ("OUTROS", "Outros")
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    foundation = models.DateField()
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name'],
                name='organization_constraint'
            )
        ]
