class DataLimit:
    """ Has the maximum number value allowed for numbers """    
    value_limit = 1000


class DataStats:
    def __init__(self, numbers_count_list: list[int], total_numbers_count: int) -> None:
        """Initializes the DataStats class

        Args:
            numbers_count_list (list[int]): A list of integers between 0 and ``DataLimit.value_limit``. The length of the list should be ``DataLimit.value_limit`` + 1.
            total_numbers_count (int): The total number of numbers in the data list. Must be equal to the sum of the numbers in ``numbers_count_list``.
        """
        self.__value_limit: int = DataLimit.value_limit
        self.__total_numbers_count: int = 0
        self.__less_numbers_count_list: dict[int, int] = dict()

        less_numbers_count = 0 # The number of numbers less than the current number
        for number in range(len(numbers_count_list)):

            self.__total_numbers_count += numbers_count_list[number]

            self.__less_numbers_count_list[number] = less_numbers_count
            less_numbers_count += numbers_count_list[number]

            self.__max_number = number

            # Iterating until the the max number is reached
            if self.__total_numbers_count == total_numbers_count:
                self.__less_numbers_count_list[self.__max_number + 1] = less_numbers_count
                break

        self.__numbers_count = numbers_count_list


    def less(self, number: int) -> int: # O(1)
        """Returns the number of values in the data that are less than the number passed in

        Args:
            number (int): The number to compare the data values to. Must be between 0 and ``self.__value_limit``.

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not between 0 and ``self.__value_limit``

        Returns:
            int: The number of values in the data that are less than the number passed in
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0 or number > self.__value_limit:
            raise ValueError('Number must be between 0 and {}'.format(self.__value_limit))

        if number > self.__max_number:
            number = self.__max_number + 1 # To avoid index out of range error. +1 to get the less numbers count from greater of it

        return self.__less_numbers_count_list[number]


    def greater(self, number: int) -> int: # O(1)
        """Returns the number of values in the data list that are greater than the number passed in

        Args:
            number (int): The number to compare the data list values to. Must be between 0 and ``self.__value_limit``.

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not between 0 and ``self.__value_limit``

        Returns:
            int: The number of values in the data list that are greater than the number passed in
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0 or number > self.__value_limit:
            raise ValueError('Number must be between 0 and {}'.format(self.__value_limit))

        return self.__total_numbers_count - self.less(number) - self.__numbers_count[number]


    def between(self, low_number: int, high_number: int = DataLimit.value_limit) -> int: # O(1)
        """Returns the number of values in the data that are between the low number and high number passed in

        Args:
            low_number (int): The low number to compare the data values to. Must be between 0 and ``self.__value_limit``.
            high_number (int, optional): The high number to compare the data values to. Must be between 0 and ``self.__value_limit``. Defaults to ``DataLimit.value_limit``.

        Raises:
            TypeError: When any of the numbers passed in are not an integer
            ValueError: When any of the numbers passed in are not between 0 and ``self.__value_limit``

        Returns:
            int: The number of values in the data that are between the low number and high number passed in
        """
        if not isinstance(low_number, int) or not isinstance(high_number, int):
            raise TypeError('The numbers must be an integer')

        if low_number < 0 or low_number > self.__value_limit or high_number < 0 or high_number > self.__value_limit:
            raise ValueError('Number must be between 0 and {}'.format(self.__value_limit))

        if low_number >= high_number:
            return 0

        return self.__total_numbers_count - self.less(low_number) - self.greater(high_number)


class DataCapture:
    def __init__(self) -> None:        
        self.__value_limit = DataLimit.value_limit
        self.__numbers_amount: int = 0
        self.__numbers_count_list: list[int] = [0] * (self.__value_limit + 1) # Build a list of zeros with the value limit as the size


    def add(self, number: int): # O(1)
        """Adds one to the number in numbers count list and increments the total numbers count

        Args:
            number (int): The number to add to the data list. Must be between 0 and ``self.__value_limit``.

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not between 0 and ``self.__value_limit``
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0 or number > self.__value_limit:
            raise ValueError('Number must be positive and less than {}'.format(self.__value_limit))
        
        self.__numbers_amount += 1
        self.__numbers_count_list[number] += 1 # Increment the count of the number in the data list


    def build_stats(self) -> DataStats: # O(n)
        """Returns a DataStats object created with the numbers count list and the total numbers count

        Returns:
            DataStats: A DataStats object created with the data list
        """
        return DataStats(self.__numbers_count_list, self.__numbers_amount)
