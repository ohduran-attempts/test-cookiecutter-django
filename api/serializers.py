from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'


class LikeByTagsSerializer(serializers.Serializer):

    field = serializers.CharField(max_length=10)
    another_field = serializers.BooleanField()

    def create(self, validated_data):
        pass
