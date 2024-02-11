import pytest
import numpy as np


def test_example():
    with pytest.raises(AssertionError) as error:
        assert False
