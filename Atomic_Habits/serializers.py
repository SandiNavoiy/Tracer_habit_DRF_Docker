from rest_framework import serializers

from Atomic_Habits.models import Habits


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = "__all__"
