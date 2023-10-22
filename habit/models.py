from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)

    place = models.CharField(max_length=200, verbose_name='Location', **NULLABLE)
    time = models.TimeField(verbose_name='Time of start')
    action = models.TextField(verbose_name='Action', **NULLABLE)
    period = models.PositiveIntegerField(default=1, verbose_name='Period(days)')
    duration_of_action = models.PositiveSmallIntegerField(verbose_name='Duration of action', **NULLABLE)

    is_pleasant = models.BooleanField(default=False, verbose_name='Is pleasant habit')
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Connected habit', **NULLABLE)
    reward = models.TextField(verbose_name='Reward for the completed action', **NULLABLE)

    is_public = models.BooleanField(default=False, verbose_name='Is public habit')

    last_reminder = models.DateTimeField(verbose_name='Last reminder', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
