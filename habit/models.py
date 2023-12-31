from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    place = models.CharField(max_length=200, verbose_name='Локация')
    time = models.TimeField(verbose_name='Время начала')
    action = models.TextField(verbose_name='Действие')
    period = models.IntegerField(default=1, verbose_name='Периодичность привычки')
    duration_of_action = models.IntegerField(verbose_name='Длительность привычки в секундах')

    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    connected_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка',
                                        **NULLABLE)
    reward = models.TextField(verbose_name='Вознаграждение за выполнение действия', **NULLABLE)

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности привычки')

    last_reminder = models.DateTimeField(verbose_name='Последнее напоминание', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
