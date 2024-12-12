class Potion:
    """
    Represents a magical potion with color and volume
    Attributes:
        color (list[int]): RGB color values in the range [0, 255]
        volume (int): Volume of the potion in magical units (non-negative)
    """
    def __init__(self, color: list[int], volume: int):
        if not (len(color) == 3 and all(0 <= c <= 255 for c in color)):
            raise ValueError("Color must be a list of three integers between 0 and 255")
        if volume < 0:
            raise ValueError("Volume must be a non-negative integer")

        self.color: list[int] = color
        self.volume: int = volume

    def mix(self, other: "Potion") -> "Potion":
        if not isinstance(other, Potion):
            raise TypeError("Argument must be an instance of Potion")

        new_volume = self.volume + other.volume
        new_color = [
            round((self.color[i] * self.volume + other.color[i] * other.volume) / new_volume)
            if new_volume > 0 else 0 for i in range(3)
        ]
        return Potion(new_color, new_volume)

port = Potion([255, 255, 255], 7)
potio_developing = Potion([51, 102, 51], 12)
new_potion = port.mix(potio_developing)

print(f"New potion color: {new_potion.color}")
print(f"New potion volume: {new_potion.volume}")

