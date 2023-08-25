from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Класс описания пагинации курсов, р
    азбивает данные на страницы на основе номера страницы.
    Клиент может указать номер страницы в запросе
    для получения нужной страницы данных"""

    page_size = 20  # количество элементов на странице
