from die import die
class Player:

    def __init__(self):
        self.dice = [die(), die(), die()]
        self.dice.sort()
        self._points = 0

    @property
    def points(self):
        return self._points

    def roll_dice(self):
        for die in self.dice:
            die.roll()
        self.dice.sort()

    def has_pair(self):
        if (self.dice[0] == self.dice[1]) or (self.dice[1] == self.dice[2]):
            self._points += 1
            return True
        return False

    def has_three_of_a_kind(self):
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self._points += 3
            return True
        return False
    
    def has_series(self):
        if (self.dice[2] - self.dice[0] == 2) and (self.dice[1] - self.dice[0] == 1):
            self._points += 2
            return True
        return False

    def __str__(self):
        return f"\nD1={self.dice[0]} D2={self.dice[1]} D3={self.dice[2]}"
