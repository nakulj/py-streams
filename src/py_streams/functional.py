from typing import Callable, TypeAlias, TypeVar

T = TypeVar('T')
U = TypeVar('U')

Mapper: TypeAlias = Callable[[T], U]
