class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
Point.reset(p)
print(p.x, p.y)
