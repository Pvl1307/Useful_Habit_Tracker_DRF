from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitUpdateTestCase(APITestCase):
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

    def test_habit_update(self):
        """Тест на редакцию привычки владельцем"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Moscow"
        }

        response = self.client.patch(
            reverse('habit:habit_update',
                    args=[self.habit.pk]),
            data=data

        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update_with_wrong_owner(self):
        user = User.objects.create(
            username='not_owner',
            password='not_owner'
        )
        self.client.force_authenticate(user=user)

        response = self.client.patch(
            reverse('habit:habit_update',
                    args=[self.habit.pk]),

        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
