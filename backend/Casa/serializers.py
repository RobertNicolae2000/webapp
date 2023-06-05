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
                  "description",
                  "date_added",
                  "get_image",
                  )
