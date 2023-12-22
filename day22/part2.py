from functools import cmp_to_key
from collections import deque

class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)

        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

        self.z1 = min(z1, z2)
        self.z2 = max(z1, z2)

        self.bellow = set()
        self.above = set()

    def fall(self):
        is_set = False
        new_z = self.z1

        for i in range(len(set_bricks) - 1, -1, -1):
            b_brick = set_bricks[i]

            if not is_set and new_z > b_brick.z2:
                new_z = b_brick.z2 + 1
            if b_brick.z2 == new_z - 1:
                if is_blocked((self.x1, self.x2), (b_brick.x1, b_brick.x2)) and is_blocked((self.y1, self.y2), (b_brick.y1, b_brick.y2)):
                    b_brick.above.add(self)
                    self.bellow.add(b_brick)
                    is_set = True
                
        if not is_set:
            new_z = 1

        self.z2 = self.z2 - (self.z1 - new_z)
        self.z1 = new_z


def is_blocked(b1,b2):
    return (b1[0] >= b2[0] and b1[0] <= b2[1]) or (b1[1] >= b2[0] and b1[1] <= b2[1]) or (b1[0] < b2[0] and b1[1] > b2[1])   


bricks = []
set_bricks = []

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

for l in data:
    brick_start, brick_end = l.strip().split("~")

    x_s, y_s, z_s = brick_start.split(",")
    x_e, y_e, z_e = brick_end.split(",")

    brick = Brick(int(x_s), int(y_s), int(z_s), int(x_e), int(y_e), int(z_e))

    bricks.append(brick)

bricks.sort(key=cmp_to_key(lambda a, b: a.z1-b.z1))

for b in bricks:
    b.fall()
    set_bricks.append(b)
    set_bricks.sort(key=cmp_to_key(lambda a, b: a.z2 - b.z2))

fallen_counter = 0

for sb in set_bricks:
    q = deque()
    fallen = {}

    q.append(sb)

    while q:
        current_brick = q.popleft()
        fallen[current_brick] = True
        
        for ab in current_brick.above:
            will_fall = True
            for bb in ab.bellow:
                if bb not in fallen:
                    will_fall = False
                    break

            if will_fall and ab not in q:
                q.append(ab)

    fallen_counter += len(fallen.keys()) - 1

print(fallen_counter)
