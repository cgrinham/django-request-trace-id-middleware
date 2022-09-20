import logging
import uuid

from django.conf import settings


def trace_id_middleware(get_response):
    """ Fetch trace id from request headers if present or create a new one. Log
    trace id and attach it to the request.
    """

    def middleware(request):
        trace_id = request.META.get(settings.TRACE_ID_NAME)
        if not trace_id:
            trace_id = str(uuid.uuid4())
            logging.info(f"Created new Trace ID: {trace_id}")
        else:
            logging.info(f"Request Trace ID: {trace_id}")
        request.trace_id = trace_id
        response = get_response(request)
        return response

    return middleware
