from django.db import models as m


class Alco(m.Model):
    name = m.TextField(unique=True)
    price = m.DecimalField(max_digits=24, decimal_places=2)
    description = m.TextField(null=True, blank=True)
    url = m.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "alco"
        ordering = ["name"]

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.name}"

    def __str__(self):
        return f"{self.pk} ({self.name})"