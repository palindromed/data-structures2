# _*_ encoding: utf-8 _*_
"""Test stack.py."""
import pytest

def test_stack():
    """Test list constructor."""
    from stack import Stack
    stacky = Stack()
    assert isinstance(stacky, Stack)


def test_start():
    """Test that empty stack has no head."""
    from stack import Stack
    stacky = Stack()
    try:
        stacky.pop().get_data()
    except IndexError:
        assert True


def test_push():
    """Test stack push function."""
    from stack import Stack
    stacky = Stack()
    stacky.push(5)
    assert stacky.head.get_data() == 5


def test_pop():
    """Test stack pop function."""
    from stack import Stack
    stacky = Stack()
    stacky.push(1)
    assert stacky.pop() == 1


def test_none():
    """Test that none object can be item in stack."""
    from stack import Stack
    stacky = Stack()
    stacky.push([3, 4, 1, "Hello world!", None])
    assert stacky.pop() is None


def test_empty():
    """Test case where an empty list is pushed to stack."""
    from stack import Stack
    stacky = Stack()
    stacky.push([])
    with pytest.raises(IndexError):
        stacky.pop().get_data()


