class MobPhone:
    def __init__(self, brand: str, size_h: int, size_w: int, price: float):
        """
        Initializes a MobPhone class that contains  brand, size, and price

        :param brand: Brand of the phone
        :param size_h: Height of the phone in mm
        :param size_w: Width of the phone in mm
        :param price: Price of the phone
        """
        self.brand = brand
        self._size_h = None
        self.size_h = size_h
        self._size_w = None
        self.size_w = size_w
        self._price = None
        self.price = price

    @property
    def size_h(self) -> int:
        """Gets phone height"""
        return self._size_h

    @size_h.setter
    def size_h(self, value: int):
        """Sets phone height within allowed range"""
        if 100 <= value <= 180:
            self._size_h = value
        else:
            pass

    @property
    def size_w(self) -> int:
        """Gets phone width"""
        return self._size_w

    @size_w.setter
    def size_w(self, value: int):
        """Sets phone width within allowed range"""
        if 20 <= value <= 120:
            self._size_w = value
        else:
            pass

    @property
    def price(self) -> float:
        """Gets phone price"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Sets phone price if non-negative"""
        if value >= 0:
            self._price = value
        else:
            pass

    def getData(self) -> str:
        """
        Returns a formatted str with phone info

        :return: Formatted str with brand, size, and price
        """
        return f"Brand: {self.brand}, Size (HxW): {self.size_h}x{self.size_w} mm, Price: ${self.price}"



p = MobPhone("Samsung", 160, 75, 800.0)
p_2 = MobPhone("Apple", 55, 70, 1200.0) #checking with not true values

print(p.getData())
print(p_2.getData())
