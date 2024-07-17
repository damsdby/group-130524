import datetime
from typing import Self


class Auto:
    def __init__(self, producer: str, auto_name: str, gasoline_consumption: float, graduation_year: int = 2020):
        self.graduation_year = graduation_year
        self.producer = producer
        self.auto_name = auto_name
        self.mileage = 0
        self.gasoline_consumption = gasoline_consumption

        def __str__(self) -> str:
            return f'<Auto called  {self.auto_name}, produced by {self.producer} >'

        __repr__ = __str__

        def __repr__(self) -> str:
            return f'<auto called {self.auto_name},has  {self.mileage} km mileage >'

        __repr__ = __str__


auto1 = Auto(auto_name='Audi', producer='Audi AG', gasoline_consumption=6.5)
auto2 = Auto(auto_name='BMW', producer='BMW AG', gasoline_consumption=6.8)
auto3 = Auto(auto_name='Volkswagen', producer='Volkswagen Group', gasoline_consumption=4.5)
