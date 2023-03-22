from typing import Callable, TypeAlias, TypeVar

T = TypeVar('T')
U = TypeVar('U')

Function: TypeAlias = Callable[[T], U]
Predicate: TypeAlias = Callable[[T], bool]
