max_number_even = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
three_largest_numbers = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
even_numbers = [1, 10, 4, 13, 22, 10, 0, 100, 12, 14, 105]
not_even_numbers = [1, 1, 3, 13, 22, 5, 17]


def find_max_even(numbers: list[int]) -> int:
    """
this function finding the largest even number in list and returning it
    :param numbers:A list of integers from which to find the largest even number
    :return: the largest even number from list and none in the case that there are no such numbers
    """
    max_number = None
    for number in numbers:
        if number / 2 == number // 2:
            if max_number is None or number > max_number:
                max_number = number

    return max_number


def find_max_three_numbers(three_numbers: list[int]) -> tuple[int, int, int]:
    """
this function finding three biggest numbers in list and returning it
    :param three_numbers: list that contains of int numbers, will find three largest of them
    :return: three largest int type numbers
    """
    sort_numbers = sorted(three_numbers, reverse=True)
    return tuple(sort_numbers[:3])


def compare_even_and_not_even(even_list: list[int], not_even_list: list[int]) -> bool:
    """
    this function comparing two results of function that are getting from two lists. In first one you can see only even
    numbers and in the second not even.
    :param even_list: will find all even numbers from the even_numbers list
    :param not_even_list:will find all not even numbers from not_even_numbers list
    :return: True in the case that in the first list are more even values than in the second list not even values
    """
    even_count = 0
    not_even_count = 0

    for el in even_list:
        if el % 2 == 0:
            even_count += 1

    for num in not_even_list:
        if num % 2 != 0:
            not_even_count += 1

    return even_count > not_even_count


the_biggest_even = find_max_even(max_number_even)
print(the_biggest_even)

largest_three_number = find_max_three_numbers(three_largest_numbers)
print(largest_three_number)

bigger_or_not = compare_even_and_not_even(even_numbers, not_even_numbers)
print(bigger_or_not)
