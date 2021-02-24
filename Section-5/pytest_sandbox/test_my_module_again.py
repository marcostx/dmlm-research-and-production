from my_module import square

import pytest

@pytest.mark.parametrize('inputs', [2, 3, 4])
def test_return(inputs):
	val = square(inputs)

	assert isinstance(val, int)