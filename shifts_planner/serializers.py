from rest_framework import serializers
from . import models


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shift
        fields = "__all__"
