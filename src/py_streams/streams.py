from typing import Generic, Iterable, Iterator, Self, TypeVar
from .functional import Function, Predicate

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):

  def __init__(self, it: Iterable[T]) -> None:
    self.it: Iterator[T] = iter(it)

  @classmethod
  def of(cls, *args: T):
    return Stream(iter(args))

  def map(self, f: Function[T, U]) -> 'Stream[U]':
    return Stream(f(t) for t in self.it)

  def filter(self, p: Predicate[T]) -> Self:
    return Stream(t for t in self.it if p(t))

  def to_list(self) -> list[T]:
    return list(self.it)
