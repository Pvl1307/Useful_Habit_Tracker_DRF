from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='test',
            password='test',
            chat_id='12341234'
        )

        self.habit = Habit.objects.create(
            place="Test",
            time='12:00',
            action="anjumaniya",
            period=7,
            duration_of_action=120,
            is_pleasant=False,
            is_public=False
        )

    def test_check_validation_choose_connected_habit_or_reward(self):
        """Тест валидатора choose_connected_habit_or_reward"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Test",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 7,
            "duration_of_action": 120,
            "is_pleasant": True,
            "connected_habit": 1,
            "reward": "eche anjumanya",
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Привычка может быть только либо со связанной привычкой, либо награждением!"
                             ]
                         }
                         )

    def test_check_validator_check_duration_of_action(self):
        """Тест валидатора check_duration_of_action"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Test",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 7,
            "duration_of_action": 200,
            "is_pleasant": True,
            "reward": "eche anjumanya",
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "duration_of_action": [
                                 "Время выполнения привычки не должно быть более 120 секунд(2 минут)!"
                             ]
                         }
                         )

    def test_check_validator_validate_just_pleasant_habit_in_connected_habit(self):
        """Тест валидатора validate_just_pleasant_habit_in_connected_habit"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Test",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 7,
            "duration_of_action": 120,
            "is_pleasant": False,
            "connected_habit": self.habit.pk,
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Связанной привычкой может быть только привычка, которая является приятной!"
                             ]
                         }
                         )

    def test_validator_validate_no_reward_or_connected_habit_for_pleasant(self):
        """Тест валидатора validate_no_reward_or_connected_habit_for_pleasant"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Test",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 7,
            "duration_of_action": 120,
            "is_pleasant": True,
            "reward": "eche anjumanya",
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "У приятной привычки не может быть вознаграждения или связанной привычки!"
                             ]
                         }
                         )

    def test_validator_check_habit_frequency(self):
        """Тест валидатора check_habit_frequency"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Denamrk",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 9,
            "duration_of_action": 120,
            "is_pleasant": True,
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "period": [
                                 "Нельзя выполнять привычку реже, чем 1 раз в неделю!"
                             ]
                         }
                         )

    def test_validator_check_habit_frequency_second_part(self):
        """Тест второй части валидатора check_habit_frequency """
        self.client.force_authenticate(user=self.user)

        data = {
            "place": "Denamrk",
            "time": "12:00",
            "action": "anjumaniya",
            "period": 0,
            "duration_of_action": 120,
            "is_pleasant": True,
            "is_public": False
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {
                             "period": [
                                 "Периодичность привычки не может равняться нулю!"
                             ]
                         }
                         )
