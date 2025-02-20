# myapp/middlewares.py


from django.core.handlers.wsgi import WSGIRequest

from core.settings import settings
from shared.exceptions import NotAuthorizedError
from utils.logger import logger
from utils.responses import EnvelopeResponse


class AuthenticationMiddelware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        if not settings.AUTHTENTICATION_ACTIVE:
            return self.get_response(request)

        path = request.path.rstrip("/")

        try:
            if path not in settings.PUBLIC_ENDPOINTS:
                api_key = request.headers.get("x-api-key", "")
                if api_key != settings.API_KEY:
                    raise NotAuthorizedError("API Key")
            else:
                logger.info(f"The endpoint {path} is public")
        except NotAuthorizedError as e:
            return EnvelopeResponse(
                errors=str(e),
                body=None,
                message=str(e),
                status_code=404,
                successful=False,
            )

        return self.get_response(request)
