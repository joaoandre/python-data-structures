import pytest
import python_data_structures


def test_project_defines_author_and_version():
    assert hasattr(python_data_structures, '__author__')
    assert hasattr(python_data_structures, '__version__')
