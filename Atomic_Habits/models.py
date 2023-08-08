from django.db import models

from users.models import NULLABLE, User


class Habits(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        **NULLABLE,
        verbose_name="пользователь"
    )
    place = models.CharField(max_length=100, **NULLABLE, verbose_name="место")
    activity = models.CharField(max_length=300, **NULLABLE, verbose_name="действие")
    reward = models.CharField(max_length=200, **NULLABLE, verbose_name="награда")
    of_publicity = models.BooleanField(default=False, verbose_name="публичность")
