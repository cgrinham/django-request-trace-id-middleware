============
Django Trace ID Middleware
============

Middleware that fetches a trace id from request headers if present or creates a new one. Logs the trace id and attaches it to the request for later use (eg. when sending a request onto another system).

***************
Settings
***************

`TRACE_ID_NAME` - The header to use for the trace id, defaults to "HTTP_TRACE_ID"

***************
Installation
***************

To install the middleware, add it to the `MIDDLEWARE` list in the django setting file.
