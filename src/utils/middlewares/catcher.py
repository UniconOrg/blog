from typing import TYPE_CHECKING

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from jwt import InvalidTokenError
from psycopg2.errors import ForeignKeyViolation

from utils.responses import EnvelopeResponse

if TYPE_CHECKING:
    from rest_framework.response import Response


class CatcherExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response: Response = self.get_response(request)
        if "/docs" in request.path or "/admin" in request.path or request.path == "/":
            return response
        data = getattr(response, "data", None)
        message = getattr(response, "message", None)
        status_code = getattr(response, "status_code", None)
        errors = getattr(response, "errors", None)
        successful = getattr(response, "successful", True)
        response_data = EnvelopeResponse(
            errors=errors,
            body=data,
            message=message,
            status_code=status_code,
            successful=successful,
        )
        return JsonResponse(data=response_data.to_dict(), status=status_code)

    def process_exception(self, request, exception):  # noqa: ARG002
        error_detail = None
        status_code = None

        if isinstance(exception, ObjectDoesNotExist):
            error_detail = {"detail": "Not found"}
            status_code = 404
        if isinstance(exception, InvalidTokenError):
            error_detail = {"detail": "InvalidTokenError"}
            status_code = 401
        elif isinstance(exception, IntegrityError):
            error_detail = {"detail": "Integrity error occurred"}
            status_code = 500
            # Check if it's a ForeignKeyViolation
            orig = getattr(exception, "orig", None)
            if orig and isinstance(orig, ForeignKeyViolation):
                error_detail = {"detail": "ForeignKeyViolation"}
                status_code = 409
        else:
            error_detail = {"detail": "Internal Server Error"}
            status_code = 500

        return EnvelopeResponse(
            errors=error_detail,
            body=None,
            message=str(exception),
            status_code=status_code,
            successful=False,
        )
