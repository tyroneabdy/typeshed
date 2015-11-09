# Stubs for os.path
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.2/library/os.path.html
# adapted for 2.7 by Michal Pokorny

from typing import overload, List, Any, Tuple, BinaryIO, TextIO, TypeVar, Callable, AnyStr

# ----- os.path variables -----
supports_unicode_filenames = False
# aliases (also in os)
curdir = ...  # type: str
pardir = ...  # type: str
sep = ...  # type: str
altsep = ...  # type: str
extsep = ...  # type: str
pathsep = ...  # type: str
defpath = ...  # type: str
devnull = ...  # type: str

# ----- os.path function stubs -----
def abspath(path: AnyStr) -> AnyStr: ...
def basename(path: AnyStr) -> AnyStr: ...

def commonprefix(list: List[AnyStr]) -> AnyStr: ...
def dirname(path: AnyStr) -> AnyStr: ...
def exists(path: unicode) -> bool: ...
def lexists(path: unicode) -> bool: ...
def expanduser(path: AnyStr) -> AnyStr: ...
def expandvars(path: AnyStr) -> AnyStr: ...

# These return float if os.stat_float_times() == True,
# but int is a subclass of float.
def getatime(path: unicode) -> float: ...
def getmtime(path: unicode) -> float: ...
def getctime(path: unicode) -> float: ...

def getsize(path: unicode) -> int: ...
def isabs(path: unicode) -> bool: ...
def isfile(path: unicode) -> bool: ...
def isdir(path: unicode) -> bool: ...
def islink(path: unicode) -> bool: ...
def ismount(path: unicode) -> bool: ...

def join(path: AnyStr, *paths: AnyStr) -> AnyStr: ...

def normcase(path: AnyStr) -> AnyStr: ...
def normpath(path: AnyStr) -> AnyStr: ...
def realpath(path: AnyStr) -> AnyStr: ...
def relpath(path: AnyStr, start: AnyStr = None) -> AnyStr: ...

def samefile(path1: unicode, path2: unicode) -> bool: ...
def sameopenfile(fp1: int, fp2: int) -> bool: ...
# TODO
#def samestat(stat1: stat_result,
#             stat2: stat_result) -> bool: ...  # Unix only

def split(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
def splitdrive(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
def splitext(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...

def splitunc(path: AnyStr) -> Tuple[AnyStr, AnyStr]: ...  # Windows only, deprecated

_T = TypeVar('_T')
def walk(path: AnyStr, visit: Callable[[_T, AnyStr, List[AnyStr]], Any], arg: _T) -> None: ...
