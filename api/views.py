from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from . import tasks
from .models import Pet
from .serializers import LikeByTagsSerializer, PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list(self, request, *args, **kwargs):
        tasks.print_message.delay('Alvaro')
        tasks.check_session.delay()
        return super().list(request, *args, **kwargs)


class LikeByTagView(generics.CreateAPIView):

    serializer_class = LikeByTagsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
