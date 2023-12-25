import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, k=0):
        try:
            if k == 0:

                r = random.choice(self.contents)
                self.contents.remove(r)
                return [r]
            else:

                r = random.sample(self.contents, k)
                for item in r:
                    self.contents.remove(item)
                return r
        except ValueError as e:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
      expected_copy = copy.deepcopy(expected_balls)
      hat_copy = copy.deepcopy(hat)
      colors_gotten = hat_copy.draw(num_balls_drawn)
      for color in colors_gotten:
        if(color in expected_copy):
          expected_copy[color]-=1

      if(all(x <= 0 for x in expected_copy.values())):
        count += 1


    return count / num_experiments
