class DataStats:
    def __init__(self, data_list: list[int], max_number: int) -> None:
        self.__max_number = max_number
        self.__data_list: list[int] = [0] * (max_number+1) # Build a list of 0's the size of the max number in the data
        
        for value in data_list:
            self.__data_list[value] += 1 # Increment the count of the values in the data list

        # Builds a list with the amount of numbers less than and greater than each index number
        self.__data_list = [{'less': sum(self.__data_list[:i]), 'greater': sum(self.__data_list[i+1:])} for i in range(len(self.__data_list))]


    def less(self, number: int) -> int: # O(1)
        """Returns the number of values in the data that are less than the number passed in

        Args:
            number (int): The number to compare the data values to

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not between 0 and the max number in the data

        Returns:
            int: The number of values in the data that are less than the number passed in
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0 or number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))
        
        return self.__data_list[number]['less']


    def between(self, low_number: int, high_number: int = 0) -> int: # O(1)
        """Returns the number of values in the data that are between the low number and high number passed in

        Args:
            low_number (int): The low number to compare the data values to
            high_number (int, optional): The high number to compare the data values to. Defaults to 0.

        Raises:
            TypeError: When any of the numbers passed in are not an integer
            ValueError: When any of the numbers passed in are not between 0 and the max number in the data

        Returns:
            int: The number of values in the data that are between the low number and high number passed in
        """
        if not isinstance(low_number, int) or not isinstance(high_number, int):
            raise TypeError('The numbers must be an integer')

        if low_number < 0 or low_number > self.__max_number or high_number < 0 or high_number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))

        if low_number >= high_number:
            return 0

        return self.__data_list[high_number + 1]['less'] - self.__data_list[low_number]['less']


    def greater(self, number: int) -> int: # O(1)
        """Returns the number of values in the data list that are greater than the number passed in

        Args:
            number (int): The number to compare the data list values to

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not between 0 and the max number in the data

        Returns:
            int: The number of values in the data list that are greater than the number passed in
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0 or number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))

        return self.__data_list[number]['greater']


class DataCapture:
    def __init__(self) -> None:
        self.__data_list: list[int] = list()


    def add(self, number: int): # O(1)
        """Adds a number to the data list and sorts the data list

        Args:
            number (int): The number to add to the data list

        Raises:
            TypeError: When the number passed in is not an integer
            ValueError: When the number passed in is not positive
        """
        if not isinstance(number, int):
            raise TypeError('The number must be an integer')

        if number < 0:
            raise ValueError('Number must be positive')
        
        self.__data_list.append(number)


    def build_stats(self) -> DataStats: # O(n)
        """Returns a DataStats object created with the data list

        Returns:
            DataStats: A DataStats object created with the data list
        """
        return DataStats(self.__data_list, max(self.__data_list))
