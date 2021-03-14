import numpy as np
from unittest import mock


def get_noisy_values():
    signal = np.array([1, 2, 3, 4, 5])
    noise = np.random.random(5)
    return signal + noise


def test_get_noisy_values():    
    with mock.patch('numpy.random.random', lambda x: 0):
        expected = np.array([1, 2, 3, 4, 5])
        values = get_noisy_values()
        # This will fail most of the time.
        assert (values == expected).all()
