#Working with setters and getters
class BouncyBall:
    def __init__(self,price,size,brand):
        self._price = price
        self._size = size
        self._brand = brand
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, int):
        self._price = new_price
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,new_size):
        if new_size in ["tiny","middle","big"] and isinstance(new_size, str):
            self._size = new_size
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def size(self,new_brand):
        if isinstance(new_brand,str):
            self._size = new_brand