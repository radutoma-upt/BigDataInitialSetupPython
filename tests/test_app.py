# tests/test_app.py
import pytest
from src.app import add, multiply  # Import from the `src` package

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

@pytest.mark.parametrize("a,b", [(None, 1), (1, None), (None, None)])
def test_add_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        add(a, b)

@pytest.mark.parametrize("a,b", [(None, 1), (1, None), (None, None)])
def test_multiply_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        multiply(a, b)
