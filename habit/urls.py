from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
