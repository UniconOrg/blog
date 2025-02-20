import uuid

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from utils.logger import logger


class LoggerMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        trace_id = request.headers.get("x-trace-id", str(uuid.uuid4()))
        caller_id = request.headers.get("x-caller-id", "000000")

        with logger.contextualize(trace_id=trace_id, caller_id=caller_id):
            logger.info(f"Received request {request.method} {request.path}")
            response = self.get_response(request)
            logger.info("Request ended")
            return response
