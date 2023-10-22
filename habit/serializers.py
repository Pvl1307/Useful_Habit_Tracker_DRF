from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
