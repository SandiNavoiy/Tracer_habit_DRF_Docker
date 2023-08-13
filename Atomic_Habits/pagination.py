from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Класс описания пагинации курсов"""

    page_size = 20  # количество страниц
