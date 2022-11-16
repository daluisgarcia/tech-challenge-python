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
        