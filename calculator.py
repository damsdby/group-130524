import json

class Calculator:
    def __init__(self):
        """
        Initializes the calculator with an empty dictionary to store operations
        """
        self.operations_dict = {}

    def add(self, a: int, b: int) -> int:
        """
        Adds two numbers and stores the operation result

        :param a: First number to add
        :param b: Second number to add
        :return: The result of the addition
        """
        result = a + b
        self.operations_dict[f"{a}+{b}"] = result
        return result

    def subtract(self, a: int, b: int) -> int:
        """
        Subtracts the second number from the first and stores the operation result

        :param a: The number to subtract from
        :param b: The number to subtract
        :return: The result of the subtraction
        """
        result = a - b
        self.operations_dict[f"{a}-{b}"] = result
        return result

    def multiply(self, a: int, b: int) -> int:
        """
        Multiplies two numbers and stores the operation result

        :param a: First number to multiply
        :param b: Second number to multiply
        :return: The result of the multiplication
        """
        result = a * b
        self.operations_dict[f"{a}*{b}"] = result
        return result

    def divide(self, a: int, b: int) -> float:
        """
        Divides the first number by the second and stores the operation result

        :param a: The dividend
        :param b: The divisor
        :return: The result of the division, or a message if dividing by zero
        """
        if b == 0:
            result = "Can't divide by zero"
        else:
            result = a / b
        self.operations_dict[f"{a}/{b}"] = result
        return result

    def quadrieren(self, a: int, b: int) -> int:
        """
        Raises the first number to the quadrieren of the second and stores the result

        :param a: The base
        :param b: The exponent
        :return: The result of the exponentiation
        """
        result = a ** b
        self.operations_dict[f"{a}**{b}"] = result
        return result

    def modulo(self, a: int, b: int) -> int:
        """
        Returns the remainder of the division of the first number by the second and stores the result

        :param a: The dividend
        :param b: The divisor
        :return: The remainder of the division
        """
        result = a % b
        self.operations_dict[f"{a}%{b}"] = result
        return result

    def save_operations(self, filename: str = "operations.json") -> None:
        """
        Saves all operations and their results to a file in JSON format

        :param filename: The name of the file where the operations will be saved
        """
        with open(filename, "w") as file:
            json.dump(self.operations_dict, file)

    def load_operations(self, filename: str = "operations.json") -> None:
        """
        Loads the operations from a file and updates the operations dict

        :param filename: The name of the file from which the operations will be loaded
        """
        with open(filename, "r") as file:
            self.operations_dict = json.load(file)

    def sum_of_first_5_results(self) -> int:
        """
        Calculates and returns the sum of the first five results stored

        :return: The sum of the first five results
        """

        return sum(list(self.operations_dict.values())[:5])



calculator = Calculator()


calculator.add(4, 17)      # 4+17 = 21
calculator.subtract(15, 5) # 15-5 = 10
calculator.multiply(8, 3)  # 8*3 = 24
calculator.divide(16, 4)   # 16/4 = 4
calculator.quadrieren(7, 2)     # 7**2 = 49
calculator.modulo(10, 3)   # 10%3 = 1


calculator.save_operations()


calculator.load_operations()


sum_of_results = calculator.sum_of_first_5_results()
print(f"сумa перших 5 і результатів дій калькулятора, що зберігаються у файлі: {sum_of_results}")
