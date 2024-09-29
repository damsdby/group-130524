testing_lists = [
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
    [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
    ["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
    ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9],
    [0, 1, None, 2, False, 1, 0],
    ["a", "b"],
    ["a"],
    [0, 0],
    [0],
    [False],
    []
]


def move_zero_values_to_the_end(*lists: list):
    """
    This function finds zero values in lists and moves them to the end of their lists. This function also
    does not consider the value False as zero because of its behavior in cycles.
    :param lists: Input lists
    :return: list with zero values moved to the end
    """
    all_together = []

    for lst in lists:
        zero_values = []
        not_zero_values = []

        for value in lst:
            if value is 0:
                zero_values.append(value)
            else:
                not_zero_values.append(value)

        all_together.append(not_zero_values + zero_values)

    return all_together


result = move_zero_values_to_the_end(*testing_lists)
for el in result:
    print(el)
