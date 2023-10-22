from rest_framework import generics

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления привычки"""
    queryset = Habit.objects.all()
