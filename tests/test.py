from py_streams.streams import Stream

def test_of():
  assert Stream.of(1, 2, 3).to_list() == [1, 2, 3]

def test_map():
  assert Stream(range(10)).map(lambda x: x + 1).to_list() == list(range(1, 11))

def test_filter():
  assert Stream(range(10)).filter(lambda x: x % 2 == 0).to_list() == list(
      range(0, 10, 2))
