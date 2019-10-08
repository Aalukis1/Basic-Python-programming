from data_encapsulation import Stopwatch

class CountingStopwatch (Stopwatch):
    def __init__(self):
        # Allow superclass to do its initialization of the
        # inherited fields
        super(CountingStopwatch, self).__init__()
        # Set number of starts to zero
        self.__count = 0
    def start(self):
        # Let superclass do its start code
        super(CountingStopwatch, self).start()
        # Count this start message
        self.__count += 1
    def reset(self):
        # Let superclass reset the inherited fields
        super(CountingStopwatch, self).reset()
        # Reset new field
        self.__count = 0
    def count(self):
        return self.__count