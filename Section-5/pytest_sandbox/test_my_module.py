from my_module import square

import pytest


@pytest.fixture
def input_value():
	return 5
	
def test_square(input_value):
	val = square(input_value)

	assert val == 25