from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import TokenAuthentication
from .models import APIRequestLog
from django.contrib.auth.models import User


# create custom middleware for tracking the application action
class ActivityLogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # authorization_header = request.META.get('HTTP_AUTHORIZATION')
        authentication = TokenAuthentication()
        try:
            user, token = authentication.authenticate(request)
            if user.is_authenticated:
                action = f"{request.method} - {request.path}"
                APIRequestLog.objects.create(user=user, action=action)
        except Exception:
            pass