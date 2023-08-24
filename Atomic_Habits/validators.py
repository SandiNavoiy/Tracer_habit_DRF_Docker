from django.core.exceptions import ValidationError
from datetime import timedelta


def validate_related_habit_and_reward(value):
    if value.relted_habbit and value.reward:
        raise ValidationError(
            "Нельзя одновременно выбрать связанную привычку и указание вознаграждения."
        )


def validate_execution_time(value):
    if value.execution_time() > 120:
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


def validate_related_habit(value):
    if value.relted_habbit and not value.relted_habbit.good_habit_sign:
        raise ValidationError(
            "В связанные привычки могут попадать только привычки с признаком приятной привычки."
        )


def validate_good_habit(value):
    if value.good_habit_sign and (value.reward or value.relted_habbit):
        raise ValidationError(
            "У приятной привычки не может быть вознаграждения или связанной привычки."
        )


def validate_periodicity(value):
    min_periodicity = timedelta(days=7)
    if value > min_periodicity:
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
