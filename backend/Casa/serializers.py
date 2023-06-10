from rest_framework import serializers
from .models import Casa

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ("user",
                  "numar_camere",
                  "adresa",
                  "pret",
                  "name",
                  "slug",
                  "numar_telefon",
                  "description",
                  "image",
                  "image2",
                  "image3",
                  "image4",
                  "image5",
                  "date_added",
                  "get_image",
                  "get_image2",
                  "get_image3",
                  "get_image4",
                  "get_image5",
                  )
