# Trohymenko Dmytro

# Task 1
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


# Task 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def make_three_dict_in_one() -> dict:
    """
    Merges three dictionaries into one.

    :return: Merged dictionary.
    """
    result = {}
    result.update(dic1)
    result.update(dic2)
    result.update(dic3)
    return result


together = make_three_dict_in_one()
print(together)


# Task 3
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check_if_exist() -> bool:
    """
    Checks if the key 5 exists in the dictionary.

    :return: True if the key 5 exists, otherwise False.
    """
    return 5 in d


res = check_if_exist()
print(res)


# Task 4
def square_numbers() -> dict:
    """
    Returns a dictionary with numbers from 1 to 15 as keys
    and their squares as values.

    :return: Dictionary of numbers and their squares.
    """
    result = {}
    for value in range(1, 16):
        result[value] = value ** 2
    return result


res = square_numbers()
print(res)


# Task 5
dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}


def calculate_summa() -> float:
    """
    Calculates the sum of all values in dict_1.

    :return: Sum of the values in the dictionary.
    """
    return sum(dict_1.values())


res = calculate_summa()
print(res)


# Task 6
dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}

delete_arg = 'Radeon 6600 MSI'

if delete_arg in dict_1:
    del dict_1[delete_arg]

print(dict_1)


# Task 7
def apply_discount(dict_1: dict, discount_rate: float) -> dict:
    """
    Aplies a discount to all prices in the dictionary.

    :param dict_1: Dictionary of products and their prices.
    :param discount_rate: Discount rate (in decimal format).
    :return: Dictionary with updated prices.
    """
    discounted_prices = {}

    for product, original_price in dict_1.items():
        discounted_price = original_price * (1 - discount_rate)
        discounted_prices[product] = discounted_price

    return discounted_prices


dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}

discount = 0.12
updated_prices = apply_discount(dict_1, discount)

print(updated_prices)


# Task 8
def make_all_together(keys: list, values: list) -> dict:
    """
    Creates a dictionary from two lists: keys and values

    :param keys: List of keys
    :param values: List of values
    :return: Dictionary created from keys and values
    """
    return dict(zip(keys, values))


keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

together = make_all_together(keys, values)
print(together)


# Task 9
def remove_duplicates(student_data: dict) -> dict:
    """
    Removes duplicates from the student data dictionary

    :param student_data: Dictionary with student data
    :return: Dictionariy with unique students
    """
    unique_students = {}

    for student_id, details in student_data.items():
        if details not in unique_students.values():
            unique_students[student_id] = details

    return unique_students


student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
}

unique_students = remove_duplicates(student_data)
print(unique_students)
