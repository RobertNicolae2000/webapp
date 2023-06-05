from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Casa
from .serializers import CasaSerializer
from django.http import Http404

from rest_framework.decorators import api_view
from django.db.models import Q

class CasaList(APIView):
    def get(self, request, format=None):
        case = Casa.objects.all()
        serializer = CasaSerializer(case, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CasaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CasaDetail(APIView):
    def get_object(self, casa_slug):
        try:
            return Casa.objects.get(slug=casa_slug)
        except Casa.DoesNotExist:
            raise Http404

    def get(self, request, casa_slug, format=None):
        casa = self.get_object(casa_slug)
        serializer = CasaSerializer(casa)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    zona = request.data.get('zona', '')
    print(zona)
    if zona:
        case = Casa.objects.filter(Q(adresa__icontains=zona))
        serializer = CasaSerializer(case, many=True)
        return Response(serializer.data)
    else:
        return Response({"case": []})


