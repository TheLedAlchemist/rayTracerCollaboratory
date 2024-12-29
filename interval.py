class interval:
    def __init__(self, min = float('inf'), max = -float('inf')):
      self.min = min
      self.max = max

    def size(self) -> float:
       return self.max - self.min

    def contains(self, x: float) -> bool:
        return self.min <= x and x <= self.max

    def surrounds(self, x: float) -> bool:
        return self.min < x and x < self.max

empty = interval()
universe = interval(-float('inf'), float('inf'))