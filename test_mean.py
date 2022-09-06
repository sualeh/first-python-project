"""Tests for mean module."""
import pytest
import mean


def test0():
    """Tests an argument of None, and ensures that no error occurs."""
    data = None
    assert mean.mean(data) is None


def test1():
    """Tests an argument of an empty list."""
    data = []
    assert mean.mean(data) is None


def test2():
    """Tests an argument of a list with just element."""
    data = [1]
    assert mean.mean(data) == 1


def test3():
    """Tests an argument of a list with positive and negative elements."""
    data = [1, -1]
    assert mean.mean(data) == 0


def test4():
    """Tests a calculated mean that is a non-integral float value."""
    data = [1, 2, 2, 5, 3]
    assert mean.mean(data) == 2.6


def test5():
    """Tests with a list of non-numeric values."""
    with pytest.raises(TypeError):
        data = [True, 'some string']
        assert mean.mean(data) == 2.6
