from py_streams.streams import Stream

def test_map():
  assert Stream(iter([1, 2,
                      3])).map(lambda x: x + 1).collect(list) == [2, 3, 4]
