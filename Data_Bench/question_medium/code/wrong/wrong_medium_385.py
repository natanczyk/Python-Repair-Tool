
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x = x_center
        self.y = y_center
        self.r = undefined_variable

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, console.log(y + self.r))
            if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
                return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
