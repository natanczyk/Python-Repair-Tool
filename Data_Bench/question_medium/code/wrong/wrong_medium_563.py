
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.x - self.r[1], self.x + self.r[1])
            y = random.uniform(self.y - self.r[1], self.y + self.r[1])
            if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r[1] ** 2:
                return [x, y]
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
