# |1|2|3
# |4|5|6
# |7|8|9


class Move:
    def __init__(self, value):
        self._value = value
        
    @property
    def value(self):
        return self._value
    
    def is_valid(self):
        return 1 <= self._value <= 9
    
    def get_row(self):
        if self.value in (1,2,3):
            return 0 # ROW 1
        elif self.value in (4,5,6):
            return 1 # ROW 2
        else:
            return 2 # ROW 3
        
    def get_column(self):
        if self.value in (1,4,7):
            return 0 # COL 1
        elif self.value in (2,5,8):
            return 1 # COL 2
        else:
            return 2 # COL 3
