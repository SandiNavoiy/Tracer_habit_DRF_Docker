from rest_framework import generics

from Atomic_Habits.models import Habits
from Atomic_Habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания привычки"""

    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Контроллер для списка привычек"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра привычки"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления привычки"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """УКонтроллер для удаления привычки"""

    queryset = Habits.objects.all()
