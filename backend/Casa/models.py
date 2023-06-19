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
    numar_telefon = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='imagini/', blank=True, null=True)
    image2 = models.ImageField(upload_to='imagini2/', blank=True, null=True)
    image3 = models.ImageField(upload_to='imagini3/', blank=True, null=True)
    image4 = models.ImageField(upload_to='imagini4/', blank=True, null=True)
    image5 = models.ImageField(upload_to='imagini5/', blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'https://imaginilicenta.blob.core.windows.net/imaginilicenta/' + self.image.name
        return ''

    def get_image2(self):
        if self.image2:
            return 'https://imaginilicenta.blob.core.windows.net/imaginilicenta/' + self.image2.name
        return ''

    def get_image3(self):
        if self.image3:
            return 'https://imaginilicenta.blob.core.windows.net/imaginilicenta/' + self.image3.name
        return ''

    def get_image4(self):
        if self.image4:
            return 'https://imaginilicenta.blob.core.windows.net/imaginilicenta/' + self.image4.name
        return ''

    def get_image5(self):
        if self.image5:
            return 'https://imaginilicenta.blob.core.windows.net/imaginilicenta/' + self.image5.name
        return ''

# https://imaginilicenta.blob.core.windows.net/imaginilicenta/imagini2/2.jpg
# https://imaginilicenta.blob.core.windows.net/imaginilicenta/imagini4/4.jpg