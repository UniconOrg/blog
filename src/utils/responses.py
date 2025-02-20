from rest_framework.response import Response


class EnvelopeResponse:
    def __init__(  # noqa: PLR0913
        self,
        errors=None,
        body=None,
        message=None,
        status_code=None,
        successful=None,
    ):
        self.errors = errors
        self.body = body
        self.message = message
        self.status_code = status_code
        self.successful = successful

    def get(self, attr):
        getattr(self, attr, None)

    def to_dict(self):
        return {
            "errors": self.errors,
            "body": self.body,
            "message": self.message,
            "status_code": self.status_code,
            "successful": self.successful,
        }


class SimpleResponse(Response):
    def __init__(self, body=None, status=None):
        data = {"errors": None, "body": body, "status_code": status}
        super().__init__(data=data, status=status)
