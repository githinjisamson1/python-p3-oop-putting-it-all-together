

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand

        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size

        self.condition = "New"

    def get_brand(self):
        return self._brand

    def get_size(self):
        return self._size

    def set_brand(self, brand):
        self._brand = brand

    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:

            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")

    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)


shoe1 = Shoe("Bata", 36)
shoe1.condition = "New"
