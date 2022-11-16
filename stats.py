class DataStats:
    def __init__(self, data_list: list[int], max_number: int) -> None:
        self.__max_number = max_number
        self.__data_list: list[int] = [0] * (max_number+1) # Build a list of 0's the size of the max number in the data
        
        for value in data_list:
            self.__data_list[value] += 1 # Increment the count of the values in the data list

        print(self.__data_list)

        # Builds a list with the amount of numbers less than and greater than each index number
        self.__data_list = [{'less': sum(self.__data_list[:i]), 'greater': sum(self.__data_list[i+1:])} for i in range(len(self.__data_list))]

        print(self.__data_list)


    def less(self, number: int) -> int: # O(1)
        '''
        Returns the number of values in the data that are less than the number passed in

        :param number: The number to compare the data values to
        :return: The number of values in the data that are less than the number passed in
        '''
        if number < 0 or number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))
        
        return self.__data_list[number]['less']


    def between(self, low_number: int, high_number: int = 0) -> int: # O(1)
        '''
        Returns the number of values in the data that are between the low number and high number passed in

        :param low_number: The low number to compare the data values to
        :param high_number: The high number to compare the data values to
        :return: The number of values in the data that are between the low number and high number passed in
        '''
        if low_number < 0 or low_number > self.__max_number or high_number < 0 or high_number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))

        if low_number >= high_number:
            return 0

        return self.__data_list[high_number + 1]['less'] - self.__data_list[low_number]['less']


    def greater(self, number: int) -> int: # O(1)
        '''
        Returns the number of values in the data list that are greater than the number passed in

        :param number: The number to compare the data list values to
        :return: The number of values in the data list that are greater than the number passed in
        '''
        if number < 0 or number > self.__max_number:
            raise ValueError('Number must be between 0 and {}'.format(self.__max_number))

        return self.__data_list[number]['greater']


class DataCapture:
    def __init__(self) -> None:
        self.__data_list: list[int] = list()


    def add(self, number: int): # O(1)
        '''
        Adds a number to the data list and sorts the data list

        :param number: The number to add to the data list
        '''
        if number < 0:
            raise ValueError('Number must be positive')
        
        self.__data_list.append(number)


    def build_stats(self) -> DataStats: # O(n)
        '''
        Returns a DataStats object created with the data list

        :return: A DataStats object created with the data list
        '''
        return DataStats(self.__data_list, max(self.__data_list))
