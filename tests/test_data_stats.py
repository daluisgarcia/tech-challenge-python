import pytest

from stats import DataStats


class TestDataStatsLessMethod:

    def test_less_method_with_no_repeated_and_no_left(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        assert data.less(3) == 2


    def test_less_method_with_some_repeated_and_no_left(self):
        data_list = [1, 1, 2, 3, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        assert data.less(3) == 3


    def test_less_method_with_some_repeated_and_some_left(self):
        data_list = [1, 2, 3, 3, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.less(2) == 1


    def test_less_method_with_no_left_and_all_repeated(self):
        data_list = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.less(3) == 5


    def test_less_method_with_some_left_and_all_repeated(self):
        data_list = [1, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.less(4) == 6


    def test_less_method_raises_value_error(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.less(6)


    def test_less_method_raises_value_error_negative_number(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.less(-1)


class TestDataStatsBetweenMethod:
    
    def test_between_method_with_no_repeated_and_no_left(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        assert data.between(2, 4) == 3


    def test_between_method_with_some_repeated_and_no_left(self):
        data_list = [1, 1, 2, 3, 3, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.between(2, 4) == 4


    def test_between_method_with_some_repeated_and_some_left(self):
        data_list = [1, 1, 2, 3, 3, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.between(2, 4) == 3

    
    def test_between_method_with_no_left_and_all_repeated(self):
        data_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.between(2, 4) == 6


    def test_between_method_with_some_left_and_all_repeated(self):
        data_list = [1, 1, 2, 2, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.between(2, 4) == 4

    
    def test_between_method_raises_value_error(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.between(6, 7)

    
    def test_between_method_raises_value_error_negative_number(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.between(-1, 7)


class TestDataStatsGreaterMethod:
    
    def test_greater_method_with_no_repeated_and_no_left(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        assert data.greater(3) == 2


    def test_greater_method_with_some_repeated_and_no_left(self):
        data_list = [1, 1, 2, 3, 3, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.greater(3) == 3


    def test_greater_method_with_some_repeated_and_some_left(self):
        data_list = [1, 1, 2, 3, 3, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.greater(3) == 2


    def test_greater_method_with_no_left_and_all_repeated(self):
        data_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.greater(3) == 4


    def test_greater_method_with_some_left_and_all_repeated(self):
        data_list = [1, 1, 2, 2, 4, 4, 5, 5]
        data = DataStats(data_list, max(data_list))
        assert data.greater(2) == 4


    def test_greater_method_raises_value_error(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.greater(6)
    

    def test_greater_method_raises_value_error_negative_number(self):
        data_list = [1, 2, 3, 4, 5]
        data = DataStats(data_list, max(data_list))
        with pytest.raises(ValueError):
            data.greater(-1)
