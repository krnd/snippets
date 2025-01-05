import inspect
from types import FrameType
from typing import Any, Dict


# Getting a variable from the caller's globals. What is a frame object?
# https://stackoverflow.com/questions/44107877/getting-a-variable-from-the-callers-globals-what-is-a-frame-object


def caller_frame(*, depth: int = 0) -> FrameType:
    _frameinfo = inspect.stack()[depth + 1]
    return _frameinfo.frame


def caller_globals(*, depth: int = 0) -> Dict[str, Any]:
    _frameinfo = inspect.stack()[depth + 1]
    return _frameinfo.frame.f_globals


def caller_locals(*, depth: int = 0) -> Dict[str, Any]:
    _frameinfo = inspect.stack()[depth + 1]
    return _frameinfo.frame.f_locals
