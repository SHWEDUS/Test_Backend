from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title
