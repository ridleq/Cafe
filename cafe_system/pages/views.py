from django.shortcuts import render


# Функция для обработки ошибок 404.
def page_not_found(request, exception):
    """
    Обрабатывает ошибки 404, когда страница не найдена.
    Возвращает страницу 404 (Не найдено).
    """
    return render(request, 'pages/404.html', status=404)


# Функция для обработки ошибок CSRF.
def csrf_failure(request, reason=''):
    """
    Обрабатывает ошибки CSRF (Cross-Site Request Forgery).
    Возвращает страницу 403 (Запрещено).
    """
    return render(request, 'pages/403csrf.html', status=403)


# Функция для обработки ошибок 500.
def server_error(request):
    """
    Обрабатывает ошибки сервера, возвращая страницу 500 (Ошибка сервера).
    """
    return render(request, 'pages/500.html', status=500)
