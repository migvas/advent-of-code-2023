# Part 1
data_file = "test.txt"

with open(data_file, "r") as f:
    lines = f.readlines()

digit_sum = 0
for line in lines:
    clean_line = line.strip()
    first_digit = ''
    last_digit = ''
    for c in clean_line:
        if c.isdigit():
            if not first_digit:
                first_digit = c

            last_digit = c

    digit_sum += int(first_digit + last_digit)

print(digit_sum)

# Part 2


class Trie:
    def __init__(self):
        self.root = {
            "next_letter": {}
        }

    def add_word(self, word, digit):
        current = self.root
        for letter in word:
            if not current["next_letter"].get(letter):
                current["next_letter"][letter] = {
                    "digit": 0,
                    "is_word": False,
                    "next_letter": {}
                }
            current = current["next_letter"][letter]

        current["is_word"] = True
        current["digit"] = str(digit)

    def search_word(self, line, starting_pos):
        current = self.root

        for i in range(starting_pos, len(line)):
            c = line[i]
            if not current["next_letter"].get(c):
                return 0

            current = current["next_letter"][c]

            if current["is_word"]:
                return current["digit"]


data_file = "data.txt"

possible_digits = ["one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]

t = Trie()

for idx, d in enumerate(possible_digits):
    t.add_word(d, idx + 1)

with open(data_file, "r") as f:
    lines = f.readlines()

digit_sum = 0

for line in lines:
    clean_line = line.strip()
    first_digit = ''
    last_digit = ''
    line_arr = list(clean_line)

    for idx, c in enumerate(line_arr):
        if c.isdigit():
            if not first_digit:
                first_digit = c

            last_digit = c

        else:
            digit = t.search_word(line_arr, idx)
            if digit:
                if not first_digit:
                    first_digit = digit

                last_digit = digit

    digit_sum += int(first_digit + last_digit)

print(digit_sum)
