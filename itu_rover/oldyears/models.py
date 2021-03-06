from django.db import models


class OldYear(models.Model):
    year = models.CharField(
        max_length=4,
        verbose_name='team year',
        unique=True,
    )

    def __str__(self):
        return str(self.year)
