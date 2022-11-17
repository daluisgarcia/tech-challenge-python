from stats import DataCapture


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    stats = capture.build_stats()

    print('Less method:', stats.less(2)) # should return 2 (only two values 3, 3 are less than 4)
    print('Between method:', stats.between(2, 4)) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
    print('Greater method:', stats.greater(4)) # should return 2 (6 and 9 are the only two values greater than 4)
