from io import StringIO
from jl import load


def test_load_simple():
    with open('test/fixtures/file1.jl') as fp:
        data = list(load(fp))
        assert len(data) == 3
        assert data[0]['id'] == 1


def test_load_string():
    fp = StringIO('{}\n  \n#')
    data = list(load(fp))
    assert len(data) == 1
