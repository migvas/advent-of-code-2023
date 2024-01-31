HAND_TYPES = ["high_card", "one_pair", "two_pair", "three_of_a_kind",
              "full_house", "four_of_a_kind", "five_of_a_kind"]

CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10
}


rank = 1
winnings = 0

class Node:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = 0
        self.get_hand_type()
        self.left = None
        self.right = None

    def get_hand_type(self):
        counter = {}
        for card in self.hand:
            if counter.get(card):
                counter[card] += 1
            else:
                counter[card] = 1
        most_frequent = 0
        second_most = 0
        add_joker = 0
        for (card, val) in counter.items():
            if card == 'J':
                add_joker = val
            elif val >= most_frequent:
                second_most = most_frequent
                most_frequent = val
            elif val >= second_most:
                second_most = val
        most_frequent += add_joker
        if most_frequent == 5:
            self.type = 6
        elif most_frequent == 4:
            self.type = 5
        elif most_frequent == 3:
            if second_most == 2:
                self.type = 4
            else:
                self.type = 3
        elif most_frequent == 2:
            if second_most == 2:
                self.type = 2
            else:
                self.type = 1
        else:
            self.type = 0


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        

        root = self.root

        while root:
            if self.is_bigger_hand(node, root):
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    return
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    return

    def is_bigger_hand(self, node, root):
        if node.type > root.type:
            return True
        elif node.type < root.type:
            return False

        for i in range(len(node.hand)):
            diff = self.points_difference(node.hand[i], root.hand[i])

            if diff > 0:
                return True
            elif diff < 0:
                return False

        return True

    def points_difference(self, card1, card2):
        card1_points = int(card1) if card1.isdigit() else CARD_VALUES[card1]

        card2_points = int(card2) if card2.isdigit() else CARD_VALUES[card2]

        return card1_points - card2_points
    
    def in_order_traversal(self, root):
        global rank
        global winnings

        if not root:
            return
        
        self.in_order_traversal(root.left)
        winnings += rank * root.bid
        rank += 1
        self.in_order_traversal(root.right)



data_file = "data.txt"

plays = Tree()
with open(data_file) as f:
    data = f.readlines()

    for l in data:
        [hand, bid] = l.strip().split()
        node = Node(hand, bid)

        plays.add_node(node)

plays.in_order_traversal(plays.root)

print(winnings)
