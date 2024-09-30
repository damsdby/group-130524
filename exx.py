# мікро_марафон1 Трохименко Дмитро
"""task_1"""


def generator_function(pair_count: int):
    """
    this function generate values 1 and 0 considering 0 firstly and 1 secondy
    :param pair_count:Number of 0, 1 pairs to generate.
    :return: list with that args(0,1) so many times, as you did in cycle
    """
    result_pairs = []
    for el in range(pair_count):
        result_pairs.append(0)
        result_pairs.append(1)

    return result_pairs


len_of_pairs = 5
all_together_check = generator_function(len_of_pairs)
print(all_together_check)

"""task_2"""
import random


def generate_list():
    """
this function generate list with chaotic values, that are limited by 20 and containing numbers such 1 and 0
    :return: list with 20 elemetns that contains values such as 1 and 0, in this list quanity of 1>quanity of 0
    """
    number_1 = random.randint(11, 20)
    number_0 = 20 - number_1
    result = [1] * number_1 + [0] * number_0
    random.shuffle(result)
    return result


print(generate_list())

"""task_3"""
even_and_not_numbers_list = [1, 22, 24, 22, 13, 15, 44, 76, 89, 66, 30, 50, 0, 1]


def say_me_even_or_not(numbers: list):
    """
    this function discover even and not even numbers and counting that values, than this func compares info and says
    which {} of numbers is bigger
    :param numbers: even and not even lists
    :return: text, that contains info about which set of values are bigger
    """
    even_numbers = sum(1 for el in numbers if el % 2 == 0)
    not_even = len(numbers) - even_numbers

    if even_numbers > not_even:
        return "У списку більше парних значень"
    elif not_even > even_numbers:
        return "У списку більше непарних значень"


result = say_me_even_or_not(even_and_not_numbers_list)
print(result)

"""task_4"""


def count_letters(text: str):
    """
    this function consider str and count amount of letters
    :param text: letterss in string
    :return: list in which you can see how many special letters contains str
    """
    text = text.lower()
    letter_count = {}

    for letter in set(text):
        if letter.isalpha():
            letter_count[letter] = text.count(letter)

    all_letters_in_list = []
    for letter, count in letter_count.items():
        all_letters_in_list.append(f'{letter} - {count}')

    return all_letters_in_list


text = 'baaAAabbaaaaBBa'
print(count_letters(text))

"""task_5"""


def encrypt_phone_number(phone_number: str) -> str:
    """
    Encrypts a phone number using the formul4

    :param phone_number: The phone number to be encrypted
    :return: The  phone number using special symbols hiding numbers
    """
    encrypted_phone_number = ''

    for digit in phone_number:
        encrypted_digit = (int(digit) + 9) % 10
        encrypted_phone_number += str(encrypted_digit)

    return encrypted_phone_number


phone_number = "067378690"
encrypted = encrypt_phone_number(phone_number)
print(encrypted)
