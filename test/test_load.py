from jl import load


def test_load_simple():
    data = list(load('test/fixtures/file1.jl'))
    assert len(data) == 3
    assert data[0]['id'] == 1
