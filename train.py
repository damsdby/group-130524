from datetime import datetime
from typing import List

class Train:
    """
    A class to represent a train with number, destination, start point, and departure time
    """

    def __init__(self, num: int, final_point: str, start_point: str, time: datetime):
        """
        Initialize the train with number, destination, start point, and departure time
        If the time is in the past, set it to the current time.

        :param num: Train num
        :param final_point: final station
        :param start_point: Starting station
        :param time: Departure time
        """
        self._num = num
        self._final_point = final_point
        self._start_point = start_point
        self._time = time if time > datetime.now() else self._set_future_time()

    def _set_future_time(self):
        """
        Set the departure time to the current time if it's in the past

        :return: Current date, time
        """
        print(f"Departure time for Train #{self._num} cannot be in the past. Setting it to current time.")
        return datetime.now()

    def info(self):
        """
        Get train detail like number, route, and departure time.

        :return: Str with train details
        """
        return (f"Train #{self._num} from {self._start_point} to {self._final_point} departs at "
                f"{self._time.strftime('%Y-%m-%d %H:%M:%S')}")

    @staticmethod
    def number_sorter(train):
        """
        Return the train number for sorting by number

        :param train: Train object
        :return: Train number
        """
        return train._num

    @staticmethod
    def destination_sorter(train):
        """
        Return destination and departure time for sorting by destination and time

        :param train: Train object
        :return: Tuple (destination, departure time)
        """
        return train._final_point, train._time

def sort_trains_by_number(trains: list) -> list:
    """
    Sort list of trains by their number

    :param trains: list of Train objects
    :return: Sorted list of trains by number
    """
    return sorted(trains, key=Train.number_sorter)

def sort_trains_by_destination(trains: list) -> list:
    """
    Sort list of trains by destination. If destinations are the same, sort by departure time

    :param trains: list of Train objects
    :return: Sorted list of trains by destination and time
    """
    return sorted(trains, key=Train.destination_sorter)

def find_train_by_number(trains: list, num: int) -> str:
    """
    Find a train by number and return its details

    :param trains: list of Train objects
    :param num: Train number to search for
    :return: Train details or message if not found
    """
    for train in trains:
        if train._num == num:
            return train.info()
    return f"No train found with number {num}."



train1 = Train(1, "Brovary", "Lviv", datetime(2024, 12, 1, 10, 0))
train2 = Train(2, "Odessa", "Lviv", datetime(2024, 11, 10, 15, 0))
train3 = Train(3, "Kyiv", "Odessa", datetime(2024, 11, 5, 9, 0))
train4 = Train(4, "Kyiv", "Lviv", datetime(2024, 11, 20, 13, 0))
train5 = Train(5, "Kharkiv", "Kyiv", datetime(2024, 11, 9, 11, 0))

trains = [train1, train2, train3, train4, train5]

sorted_by_number = sort_trains_by_number(trains)
print("Trains sorted by number:")
for train in sorted_by_number:
    print(train.info())


sorted_by_destination = sort_trains_by_destination(trains)
print("\nTrains sorted by destination and time:")
for train in sorted_by_destination:
    print(train.info())

train_number = 106
print("\n" + find_train_by_number(trains, train_number))
