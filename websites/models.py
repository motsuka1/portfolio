from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField()
    url_github = models.URLField(blank=True, null=True)
    image = models.ImageField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
