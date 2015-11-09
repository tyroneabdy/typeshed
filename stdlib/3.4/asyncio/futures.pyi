from typing import Any, Callable, TypeVar, List, Generic, Iterable, Iterator
from asyncio.events import AbstractEventLoop
# __all__ = ['CancelledError', 'TimeoutError',
#            'InvalidStateError',
#            'wrap_future',
#            ]
__all__ = ['Future']

_T = TypeVar('_T')

class _TracebackLogger:
    __slots__ = [] # type: List[str]
    exc = Any # Exception
    tb = [] # type: List[str]
    def __init__(self, exc: Any, loop: AbstractEventLoop) -> None: ...
    def activate(self) -> None: ...
    def clear(self) -> None: ...
    def __del__(self) -> None: ...

class Future(Iterator[_T], Generic[_T]):
    _state = ...  # type: str
    _exception = Any #Exception
    _blocking = False
    _log_traceback = False
    _tb_logger = _TracebackLogger
    def __init__(self, *, loop: AbstractEventLoop = None) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...
    def cancel(self) -> bool: ...
    def _schedule_callbacks(self) -> None: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> _T: ...
    def exception(self) -> Any: ...
    def add_done_callback(self, fn: Callable[[Future[_T]], Any]) -> None: ...
    def remove_done_callback(self, fn: Callable[[Future[_T]], Any]) -> int: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Any) -> None: ...
    def _copy_state(self, other: Any) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __next__(self) -> _T: ...
