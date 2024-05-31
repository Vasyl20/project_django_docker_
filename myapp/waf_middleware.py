from django.http import HttpResponseForbidden

class CustomWAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # код для перевірки та фільтрації запитів
        blocked_ips = ['122.0.0.1', '192.160.1.1']  # Приклад заблокованих IP-адрес
        if request.META['REMOTE_ADDR'] in blocked_ips:
            return HttpResponseForbidden("Access forbidden")
        
        response = self.get_response(request)
        return response
    
