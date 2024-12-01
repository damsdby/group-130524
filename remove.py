class List:
    def __init__(self, data):
        """
        Class initializer


        :param data: List that will be used in class
        """
        self.data = data

    def remove_values(self, val):
        """
        Method for del el from list які that are in val list

        :param val: List values that must be deleted from self.data
        """


        self.data = [item for item in self.data if item not in val]

    def __str__(self):
        """
        returns str for comfortable using
        """
        return str(self.data)





list_1 = List([1, 8, 2, 3, 1, 2, 3, 4])
val = [1, 3, 6, 2]


list_1.remove_values(val)




print("list:", list_1)
print("list_after_del:", list_1)
