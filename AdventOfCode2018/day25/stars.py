
class Star:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __repr__(self):
        return f'Star({self.x}, {self.y}, {self.z}, {self.w})'

    def __eq__(self, other):
        if not isinstance(other, Star):
            return False
        return self.x == other.x and self.y == other.y and \
            self.z == other.z and self.w == other.w

    def __hash__(self):
        return hash([self.x, self.y, self.z, self.w])
        
    def manhattan_dist(self, other):
        if not isinstance(other, Star):
            raise TypeError
        return abs(self.x - other.x) + abs(self.y - other.y) + \
                abs(self.z - other.z) + abs(self.w - other.w)
    

class Constellation:
    def __init__(self):
        self.stars = []

    def __repr__(self):
        return str(self.stars)

    def add_star(self, star):
        if not isinstance(star, Star):
            raise TypeError
        self.stars.append(star)