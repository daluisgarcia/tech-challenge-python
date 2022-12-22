import pytest

from stats import DataCapture

class TestDataCapture:

    def test_data_capture_basic_flow(self):
        '''Asserts that the data capture class works as expected'''
        data_to_add = [3, 9, 3, 4, 6]

        capture = DataCapture()

        for number in data_to_add:
            capture.add(number)

        stats = capture.build_stats()

        assert stats.less(4) == 2
        assert stats.between(3, 6) == 4
        assert stats.greater(4) == 2


    def test_data_capture_adding_non_integers(self):
        '''Asserts that the data capture class raises a TypeError when adding non-integer values'''

        capture = DataCapture()
        with pytest.raises(TypeError):
            capture.add('a')

        with pytest.raises(TypeError):
            capture.add([])


    def test_data_capture_adding_negative_numbers(self):
        '''Asserts that the data capture class raises a ValueError when adding negative numbers'''

        capture = DataCapture()
        with pytest.raises(ValueError):
            capture.add(-1)

        with pytest.raises(ValueError):
            capture.add(-1000)

    
    def test_data_capture_adding_values_greater_then_a_thousand(self):
        '''Asserts that the data capture class raises a ValueError when adding values greater than a thousand'''

        capture = DataCapture()
        with pytest.raises(ValueError):
            capture.add(1001)

        with pytest.raises(ValueError):
            capture.add(1000000)
        
        