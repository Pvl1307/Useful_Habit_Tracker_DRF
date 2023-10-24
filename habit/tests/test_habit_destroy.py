from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitDestroyTestCase(APITestCase):
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

    def test_habit_destroy_wrong_owner(self):
        """Тест на проверку удаления объекта чужим пользователем"""
        user = User.objects.create(
            username='not_owner',
            password='not_owner'
        )
        self.client.force_authenticate(user=user)

        response = self.client.delete(
            reverse('habit:habit_delete',
                    args=[self.habit.pk]),

        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_habit_destroy(self):
        """Тест на удаление объекта владельцем"""
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('habit:habit_delete',
                    args=[self.habit.pk]),
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
