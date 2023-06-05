from django.db import models
from django.contrib.auth.models import User


class Casa(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='casa', on_delete=models.CASCADE)
    numar_camere = models.DecimalField(max_digits=2, decimal_places=0)
    adresa = models.CharField(max_length=255)
    pret = models.DecimalField(max_digits=8, decimal_places=0)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='imagini/', blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://localhost:8000' + self.image.url
        return ''
