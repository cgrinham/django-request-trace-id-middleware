from django.conf import settings

settings.TRACE_ID_NAME = getattr(settings, 'TRACE_ID_NAME', "HTTP_TRACE_ID")
