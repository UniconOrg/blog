from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import request, status, viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.settings import settings
from utils.logger import logger


class HealthCheckViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    @method_decorator(never_cache)
    @action(
        detail=False,
        methods=["get"],
        url_name="",
    )
    def health(self, _: request.Request, __: str | None = None):
        logger.info("Request to Health")
        body = {
            "detail": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "timestamp": settings.TIMESTAMP,
        }
        response = Response(data=body, status=status.HTTP_200_OK)
        response.message = "The health check system is alive"
        return response
