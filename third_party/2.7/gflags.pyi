from typing import Any, Callable, Dict, Iterable, IO, List, Union
from types import ModuleType

class FlagsError(Exception): ...

class DuplicateFlag(FlagsError): ...

class CantOpenFlagFileError(FlagsError): ...

class DuplicateFlagCannotPropagateNoneToSwig(DuplicateFlag): ...

class DuplicateFlagError(DuplicateFlag):
      def __init__(self, flagname: str, flag_values: FlagValues, other_flag_values: FlagValues = None) -> None: ...

class IllegalFlagValue(FlagsError): ...

class UnrecognizedFlag(FlagsError): ...

class UnrecognizedFlagError(UnrecognizedFlag):
    def __init__(self, flagname: str, flagvalue: str = '') -> None: ...

def GetHelpWidth() -> int: ...
def CutCommonSpacePrefix(text) -> str: ...
def TextWrap(text: str, length: int = None, indent: str = '', firstline_indent: str = None, tabs: str = '    ') -> str: ...
def DocToHelp(doc: str) -> str: ...

class FlagValues:
    def __init__(self) -> None: ...
    def UseGnuGetOpt(self, use_gnu_getopt: bool = True) -> None: ...
    def IsGnuGetOpt(self) -> bool: ...
# TODO dict type
    def FlagDict(self) -> dict: ...
    def FlagsByModuleDict(self) -> Dict[str, List[Flag]]: ...
    def FlagsByModuleIdDict(self) -> Dict[int, List[Flag]]: ...
    def KeyFlagsByModuleDict(self) -> Dict[str, List[Flag]]: ...
    def FindModuleDefiningFlag(self, flagname: str, default: str = None) -> str: ...
    def FindModuleIdDefiningFlag(self, flagname: str, default: int = None) -> int: ...
    def AppendFlagValues(self, flag_values: FlagValues) -> None: ...
    def RemoveFlagValues(self, flag_values: FlagValues) -> None: ...
    def __setitem__(self, name: str, flag: Flag) -> None: ...
    def __getitem__(self, name: str) -> Flag: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any): ...
    def __delattr__(self, flag_name: str) -> None: ...
    def SetDefault(self, name: str, value: Any) -> None: ...
    def __contains__(self, name: str) -> bool: ...
    has_key = __contains__
    def __iter__(self) -> Iterable[str]: ...
    def __call__(self, argv: List[str]) -> List[str]: ...
    def Reset(self) -> None: ...
    def RegisteredFlags(self) -> List[str]: ...
    def FlagValuesDict(self) -> Dict[str, Any]: ...
    def __str__(self) -> str: ...
    def GetHelp(self, prefix: str = '') -> str: ...
    def ModuleHelp(self, module: Union[ModuleType, str]) -> str: ...
    def MainModuleHelp(self) -> str: ...
    def get(self, name: str, default: Any) -> Any: ...
    def ShortestUniquePrefixes(self, fl: Dict[str, Flag]) -> Dict[str, str]: ...
    def ExtractFilename(self, flagfile_str: str) -> str: ...
    def ReadFlagsFromFiles(self, argv: List[str], force_gnu: bool = True) -> List[str]: ...
    def FlagsIntoString(self) -> str: ...
    def AppendFlagsIntoFile(self, filename: str) -> None: ...
    def WriteHelpInXMLFormat(self, outfile: IO[str] = None) -> None: ...
  # TODO validator: gflags_validators.Validator
    def AddValidator(self, validator: Any) -> None: ...

FLAGS = None  # type: FlagValues

class Flag:
    name = ...  # type: str
    default = None  # type: Any
    default_as_str = ...  # type: str
    value = None  # type: Any
    help = ...  # type: str
    short_name = ...  # type: str
    boolean = False
    present = False
    parser = None  # type: ArgumentParser
    serializer = None  # type: ArgumentSerializer
    allow_override = False

    def __init__(self, parser: ArgumentParser, serializer: ArgumentSerializer, name: str,
               default: str, help_string: str, short_name: str = None, boolean: bool = False,
               allow_override: bool = False) -> None: ...
    def Parse(self, argument: Any) -> Any: ...
    def Unparse(self) -> None: ...
    def Serialize(self) -> str: ...
    def SetDefault(self, value: Any) -> None: ...
    def Type(self) -> str: ...
    def WriteInfoInXMLFormat(self, outfile: IO[str], module_name: str, is_key: bool = False, indent: str = '') -> None: ...

class ArgumentParser(object):
    syntactic_help = ...  # type: str
# TODO what is this
    def Parse(self, argument: Any) -> Any: ...
    def Type(self) -> str: ...
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str) -> None: ...

class ArgumentSerializer:
    def Serialize(self, value: Any) -> unicode: ...

class ListSerializer(ArgumentSerializer):
    def __init__(self, list_sep: str) -> None: ...
    def Serialize(self, value: List[Any]) -> str: ...

def RegisterValidator(flag_name: str,
                      checker: Callable[[Any], bool],
                      message: str = 'Flag validation failed',
                      flag_values: FlagValues = ...) -> None: ...
def MarkFlagAsRequired(flag_name: str, flag_values: FlagValues = ...) -> None: ...



def DEFINE(parser: ArgumentParser, name: str, default: Any, help: str,
           flag_values: FlagValues = ..., serializer: ArgumentSerializer = None, **args: Any) -> None: ...
def DEFINE_flag(flag: Flag, flag_values: FlagValues = ...) -> None: ...
def DECLARE_key_flag(flag_name: str, flag_values: FlagValues = ...) -> None: ...
def ADOPT_module_key_flags(module: ModuleType, flag_values: FlagValues = ...) -> None: ...
def DEFINE_string(name: str, default: str, help: str, flag_values: FlagValues = ..., **args: Any): ...

class BooleanParser(ArgumentParser):
    def Convert(self, argument: Any) -> bool: ...
    def Parse(self, argument: Any) -> bool: ...
    def Type(self) -> str: ...

class BooleanFlag(Flag):
    def __init__(self, name: str, default: bool, help: str, short_name=None, **args: Any) -> None: ...

def DEFINE_boolean(name: str, default: bool, help: str, flag_values: FlagValues = ..., **args: Any) -> None: ...

DEFINE_bool = DEFINE_boolean

class HelpFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class HelpXMLFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class HelpshortFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class NumericParser(ArgumentParser):
    def IsOutsideBounds(self, val: float) -> bool: ...
    def Parse(self, argument: Any) -> float: ...
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str) -> None: ...
    def Convert(self, argument: Any) -> Any: ...

class FloatParser(NumericParser):
    number_article = ...  # type: str
    number_name = ...  # type: str
    syntactic_help = ...  # type: str
    def __init__(self, lower_bound: float = None, upper_bound: float = None) -> None: ...
    def Convert(self, argument: Any) -> float: ...
    def Type(self) -> str: ...

def DEFINE_float(name: str, default: float, help: str, lower_bound: float = None,
                 upper_bound: float = None, flag_values: FlagValues = ..., **args: Any) -> None: ...

class IntegerParser(NumericParser):
    number_article = ...  # type: str
    number_name = ...  # type: str
    syntactic_help = ...  # type: str
    def __init__(self, lower_bound: int = None, upper_bound: int = None) -> None: ...
    def Convert(self, argument: Any) -> int: ...
    def Type(self) -> str: ...

def DEFINE_integer(name: str, default: int, help: str, lower_bound: int = None,
                   upper_bound: int = None, flag_values: FlagValues = ..., **args: Any) -> None: ...

class EnumParser(ArgumentParser):
    def __init__(self, enum_values: List[str]) -> None: ...
    def Parse(self, argument: Any) -> Any: ...
    def Type(self) -> str: ...

class EnumFlag(Flag):
    def __init__(self, name: str, default: str, help: str, enum_values: List[str],
               short_name: str, **args: Any) -> None: ...

def DEFINE_enum(name: str, default: str, enum_values: List[str], help: str,
                flag_values: FlagValues = ..., **args: Any) -> None: ...

class BaseListParser(ArgumentParser):
    def __init__(self, token: str = None, name: str = None) -> None: ...
    def Parse(self, argument: Any) -> list: ...
    def Type(self) -> str: ...

class ListParser(BaseListParser):
    def __init__(self) -> None: ...
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str): ...

class WhitespaceSeparatedListParser(BaseListParser):
    def __init__(self) -> None: ...
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str): ...

def DEFINE_list(name: str, default: List[str], help: str, flag_values: FlagValues = ..., **args: Any) -> None: ...
def DEFINE_spaceseplist(name: str, default: List[str], help: str, flag_values: FlagValues = ..., **args: Any) -> None: ...

class MultiFlag(Flag):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def Parse(self, arguments: Any) -> None: ...
    def Serialize(self) -> str: ...
    def Type(self) -> str: ...

def DEFINE_multistring(name: str, default: Union[str, List[str]], help: str,
                       flag_values: FlagValues = ..., **args: Any) -> None: ...

def DEFINE_multi_int(name: str, default: Union[int, List[int]], help: str, lower_bound: int = None,
                     upper_bound: int = None, flag_values: FlagValues = FLAGS, **args: Any) -> None: ...


def DEFINE_multi_float(name: str, default: Union[float, List[float]], help: str,
                       lower_bound: float = None, upper_bound: float = None,
                       flag_values: FlagValues = ..., **args: Any) -> None: ...
