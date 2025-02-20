from typing import Any

from loguru._logger import Core, Logger


class CustomLogger(Logger):
    def contextualize(self, **kwargs: Any):
        self.trace_id = kwargs.get("trace_id")
        self.caller_id = kwargs.get("caller_id")

        return super().contextualize(**kwargs)


logger = CustomLogger(
    core=Core(),
    exception=None,
    depth=0,
    record=False,
    lazy=False,
    colors=False,
    raw=False,
    capture=True,
    patchers=[],
    extra={},
)
