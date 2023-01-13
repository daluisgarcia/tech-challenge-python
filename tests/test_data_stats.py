import pytest

from stats import DataStats, DataLimit


class TestDataStatsLessMethod:
    def __init_number_count(self) -> list[int]:
        return [0] * (DataLimit.value_limit + 1)


    def test_less_method_with_no_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        assert data.less(3) == 2


    def test_less_method_with_some_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 1
        number_count[3] = 2
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        assert data.less(3) == 3


    def test_less_method_with_some_repeated_and_some_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.less(2) == 1


    def test_less_method_with_no_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 3
        number_count[2] = 2
        number_count[3] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.less(3) == 5


    def test_less_method_with_some_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 4
        number_count[2] = 2
        number_count[4] = 3
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.less(100) == 11


    def test_less_method_raises_type_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(TypeError):
            data.less('a')


    def test_less_method_raises_value_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.less(1001)


    def test_less_method_raises_value_error_negative_number(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.less(-1)


class TestDataStatsBetweenMethod:
    def __init_number_count(self) -> list[int]:
        return [0] * (DataLimit.value_limit + 1)
    
    def test_between_method_with_no_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        assert data.between(2, 4) == 3


    def test_between_method_with_some_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 1
        number_count[3] = 2
        number_count[4] = 1
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.between(2, 4) == 4


    def test_between_method_with_some_repeated_and_some_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 1
        number_count[3] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.between(2, 4) == 3

    
    def test_between_method_with_no_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 2
        number_count[3] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.between(2, 4) == 6


    def test_between_method_with_some_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.between(2, 1000) == 6


    def test_between_method_raises_type_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(TypeError):
            data.between('a', 1)

    
    def test_between_method_raises_value_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.between(3, 1001)

    
    def test_between_method_raises_value_error_negative_number(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.between(-1, 7)


class TestDataStatsGreaterMethod:
    def __init_number_count(self) -> list[int]:
        return [0] * (DataLimit.value_limit + 1)
    
    def test_greater_method_with_no_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        assert data.greater(3) == 2


    def test_greater_method_with_some_repeated_and_no_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 1
        number_count[3] = 2
        number_count[4] = 1
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.greater(3) == 3


    def test_greater_method_with_some_repeated_and_some_left(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 1
        number_count[3] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.greater(3) == 2


    def test_greater_method_with_no_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 2
        number_count[3] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.greater(3) == 4


    def test_greater_method_with_some_left_and_all_repeated(self):
        number_count = self.__init_number_count()
        number_count[1] = 2
        number_count[2] = 2
        number_count[4] = 2
        number_count[5] = 2
        data = DataStats(number_count)
        assert data.greater(2) == 4


    def test_greater_method_raises_type_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(TypeError):
            data.greater('a')


    def test_greater_method_raises_value_error(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.greater(1001)
    

    def test_greater_method_raises_value_error_negative_number(self):
        number_count = self.__init_number_count()
        number_count[1] = 1
        number_count[2] = 1
        number_count[3] = 1
        number_count[4] = 1
        number_count[5] = 1
        data = DataStats(number_count)
        with pytest.raises(ValueError):
            data.greater(-1)
