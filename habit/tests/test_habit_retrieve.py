from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitRetrieveTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='test',
            password='test',
            chat_id='12341234'
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

    def test_habit_retrieve(self):
        """Тест на получение одной из привычек владельца"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('habit:habit_detail',
                    args=[self.habit.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve_wrong_owner(self):
        """Тест на проверку получения объекта чужим пользователем"""
        user = User.objects.create(
            username='not_owner',
            password='not_owner',
            chat_id='1239894'
        )
        self.client.force_authenticate(user=user)

        response = self.client.get(
            reverse('habit:habit_detail',
                    args=[self.habit.pk]),

        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
