from python_data_structures.stack.stack_array import ArrayStack
from python_data_structures.__exceptions__ import Empty
import pytest


class TestArrayStack(object):
    def test_init(self):
        a = ArrayStack()
        assert len(a) == 0

    def test_push(self):
        a = ArrayStack()
        a.push("foo")
        assert not a.is_empty()

    def test_is_empty(self):
        a = ArrayStack()
        assert a.is_empty()
        a.push("foo")
        assert not a.is_empty()

    def test_top(self):
        a = ArrayStack()
        with pytest.raises(Empty):
            a.top()
        a.push("foo")
        assert a.top() == "foo"

    def test_pop(self):
        a = ArrayStack()
        with pytest.raises(Empty):
            a.pop()
        a.push("foo")
        assert a.pop() == "foo"
        assert a.is_empty()
