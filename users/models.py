from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Класс Юзера"""

    def save(self, *args, **kwargs):
        """Создание пароля и его хеширование"""
        self.set_password(self.password)
        super().save(*args, **kwargs)
