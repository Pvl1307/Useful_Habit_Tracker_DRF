from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='test',
            password='test'
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Test',
            time='12:00:00',
            action='Test',
            period=3,
            duration_of_action=60,
            is_pleasant=False
        )

    def test_get_habit_list(self):
        """Тест на получения списка привычек владельца"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('habit:habit_list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "period": self.habit.period,
                        "duration_of_action": self.habit.duration_of_action,
                        "is_pleasant": self.habit.is_pleasant,
                        "connected_habit": self.habit.connected_habit,
                        "is_public": self.habit.is_public,
                        "last_reminder": self.habit.last_reminder,
                        "owner": self.habit.owner.pk,
                        "reward": self.habit.reward
                    }
                ]
            }
        )
