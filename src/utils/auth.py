import types

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer

from core.settings import settings

X_API_KEY_PARAMETER = openapi.Parameter(
    "X-API-Key",
    openapi.IN_HEADER,
    description="API Key",
    type=openapi.TYPE_STRING,
    required=settings.AUTHTENTICATION_ACTIVE,
)

X_SERVICE_NAME_PARAMETER = openapi.Parameter(
    "X-Service-Name",
    openapi.IN_HEADER,
    description="Service Name",
    type=openapi.TYPE_STRING,
    required=settings.AUTHTENTICATION_ACTIVE,
)

X_TRACE_ID_PARAMETER = openapi.Parameter(
    "x-trace-id",
    openapi.IN_HEADER,
    description="Trace ID",
    type=openapi.TYPE_STRING,
    required=False,
)

X_CALLER_ID_PARAMETER = openapi.Parameter(
    "x-caller-id",
    openapi.IN_HEADER,
    description="Caller ID",
    type=openapi.TYPE_STRING,
    required=False,
)

DEFAULT_PARAMETERS = [
    X_API_KEY_PARAMETER,
    X_TRACE_ID_PARAMETER,
    X_CALLER_ID_PARAMETER,
]


def apply_swagger_decorator(dct, tags, manual_parameters=[]):
    for attr, value in dct.items():
        if callable(value):
            if hasattr(value, "_swagger_auto_schema"):
                original_func = value.original_func
            else:
                original_func = value

            new_func = types.FunctionType(
                original_func.__code__,
                original_func.__globals__,
                name=original_func.__name__,
                argdefs=original_func.__defaults__,
                closure=original_func.__closure__,
            )

            new_func = swagger_auto_schema(
                manual_parameters=DEFAULT_PARAMETERS + manual_parameters,
                operation_description=f"Descripción de la operación {attr}",
                responses={200: "Respuesta de éxito"},
                tags=tags,
            )(new_func)

            new_func.original_func = original_func
            dct[attr] = new_func


class SwaggerAutoSchemaMeta(type):
    def __new__(cls, name, bases, dct):
        tags = [dct.get("tag")]
        manual_parameters = dct.get("manual_parameters", [])

        for base in bases:
            if base.__name__ == "SwaggerAutoSchemaViewSetMixin":
                base_dct = {
                    attr: value
                    for attr, value in base.__dict__.items()
                    if callable(value)
                }
                apply_swagger_decorator(base_dct, tags, manual_parameters)
                dct.update(base_dct)
                return super().__new__(cls, name, bases, dct)

        if name != "SwaggerAutoSchemaViewSetMixin":
            apply_swagger_decorator(dct, tags)

        return super().__new__(cls, name, bases, dct)


class SwaggerAutoSchemaViewSetMixin:
    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.message = "Service list successfully"
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.message = "Service create successfully"
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.message = "Service retrieve successfully"
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.message = "Service update successfully"
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        response.message = "Service partial_update successfully"
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.message = "Service destroy successfully"
        return response
