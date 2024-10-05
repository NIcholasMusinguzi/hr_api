# hr_api/middleware.py

from datetime import datetime
from .models import APIRequestLog

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before the view is called
        response = None
        status_code = None

        # Process the request and get the response
        try:
            response = self.get_response(request)
            status_code = response.status_code
        except Exception as e:
            # Log failed request with 500 error
            status_code = 500

        # Log request
        APIRequestLog.objects.create(
            method=request.method,
            path=request.path,
            status_code=status_code,
            timestamp=datetime.now(),
            ip_address=request.META.get('REMOTE_ADDR'),
            user=request.user if request.user.is_authenticated else None
        )

        return response
