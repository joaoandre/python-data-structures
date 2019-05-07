from python_data_structures.stack.algorithms import reverse_data, is_matched
import pytest


class TestStackAlgotithms(object):
    def test_reverse_data(self):
        data = "foobar123"

        assert reverse_data(data) == "321raboof"

    @pytest.mark.parametrize(
        "expr, expected",
        [
            ("()", True),
            ("{}", True),
            ("[]", True),
            ("", True),
            ("[)]", False),
            ("([)]", False),
            ("{([({})])}", True),
            ("{([{})])}", False),
        ],
    )
    def test_is_matched(self, expr, expected):
        assert is_matched(expr) == expected
