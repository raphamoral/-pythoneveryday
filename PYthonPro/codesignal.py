import statistics

class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        pass

    def add(self, value: int) -> None:
        self.append(value)
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        return self
    def delete(self, value: int) -> bool:
        if (value in self):

            self.remove(value)
            return True
        else:
            return False


        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method


    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        media = sum(self)//len(self)
        # TODO: implement this method
        return media
