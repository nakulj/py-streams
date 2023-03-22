from typing import Generic, Iterator, TypeVar
from .functional import Function

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):

  def __init__(self, it: Iterator[T]) -> None:
    self.it: Iterator[T] = it

  def map(self, f: Function[T, U]) -> 'Stream[U]':
    return Stream(f(t) for t in self.it)

  def to_list(self) -> list[T]:
    return list(self.it)
