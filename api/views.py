from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Pet
from .serializers import PetSerializer
from .tasks import check_session, print_message

User = get_user_model()


class PetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list(self, request, *args, **kwargs):
        print_message.delay('Alvaro')
        check_session.delay()
        return super().list(request, *args, **kwargs)
