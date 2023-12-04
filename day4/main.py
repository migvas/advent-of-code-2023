from collections import deque
from datetime import datetime

data_file = "data.txt"

with open(data_file, "r") as f:
    cards = f.readlines()

# Part 1
sum_points = 0

for card in cards:
    card = card.strip()

    numbers = card.split(":")[1]

    winning_numbers = numbers.split("|")[0].split()

    numbers_you_have = numbers.split("|")[1].split()

    matching_numbers = 0

    winning_obj = {}

    for num in winning_numbers:
        winning_obj[num] = True

    for num in numbers_you_have:
        if winning_obj.get(num):
            matching_numbers += 1

    if matching_numbers:
        sum_points += 2 ** (matching_numbers - 1)

print(sum_points)

# Part 2

# First try (slowest)
start=datetime.now()
q = deque([i for i in range(len(cards))])
total_scratchcards = 0
card_result = {}
while len(q):
    card_idx = q.popleft()
    total_scratchcards += 1
    if card_result.get(card_idx):
        q.extend(card_result[card_idx])
    else:
        card = cards[card_idx].strip()
        numbers = card.split(":")[1]

        winning_numbers = numbers.split("|")[0].split()

        numbers_you_have = numbers.split("|")[1].split()

        matching_numbers = 0

        winning_obj = {}

        for num in winning_numbers:
            winning_obj[num] = True

        for num in numbers_you_have:
            if winning_obj.get(num):
                matching_numbers += 1
        
        if matching_numbers:
            copy_list = [i for i in range(card_idx + 1, card_idx + matching_numbers + 1)]
            card_result[card_idx] = copy_list
            q.extend(copy_list)

print(total_scratchcards)
print(datetime.now()-start)

# Second try (fastest)
start=datetime.now()
total_scratchcards = 0
card_result = {}

def compute_scratchcards(idx):
    if card_result.get(idx):
        return card_result[idx]
    
    card = cards[idx].strip()
    numbers = card.split(":")[1]

    winning_numbers = numbers.split("|")[0].split()

    numbers_you_have = numbers.split("|")[1].split()

    matching_numbers = 0

    winning_obj = {}

    for num in winning_numbers:
        winning_obj[num] = True

    for num in numbers_you_have:
        if winning_obj.get(num):
            matching_numbers += 1

    num_scratchcards = 1
    if matching_numbers:
        for i in range(idx + 1, idx + matching_numbers + 1):
            num_scratchcards += compute_scratchcards(i)
    card_result[idx] = num_scratchcards
    return num_scratchcards

for i in range(len(cards)):
    total_scratchcards += compute_scratchcards(i)

print(total_scratchcards)
print(datetime.now()-start)