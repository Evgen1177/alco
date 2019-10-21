from django.db import models as m


class Technology(m.Model):
    name = m.TextField(unique=True)
    url = m.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "technologies"
        ordering = ["id"]
        #ordering = ["name"] #  по имени сортировка

    def __repr__(self):
        return f"Technology #{self.pk}: {self.name}"

    def __str__(self):
        # return repr(self)
        return f"{self.pk}: {self.name}"
