from typing import Generic, Iterator, TypeVar
from .functional import Mapper

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):

  def __init__(self, it: Iterator[T]) -> None:
    self.it: Iterator[T] = it

  def map(self, mapper: Mapper[T, U]) -> 'Stream[U]':
    return Stream(mapper(t) for t in self.it)

  def collect(self, collector):
    return collector(self.it)
