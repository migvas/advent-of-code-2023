from collections import deque
from math import lcm

class Broadcaster:
    def __init__(self):
        self.outputs = []
        self.type = "broadcaster"

    def add_output(self, output):
        self.outputs.append(output)

    def broadcast(self, signal):
        return {
            "signal": signal,
            "outputs": self.outputs
        }


class Flipflop:
    def __init__(self):
        self.is_on = False
        self.outputs = []
        self.type = "flipflop"

    def add_output(self, output):
        self.outputs.append(output)

    def broadcast(self, signal):
        if signal == "l":
            self.is_on = not self.is_on

            signal = "h" if self.is_on else "l"

            return {
                "signal": signal,
                "outputs": self.outputs
            }
        
        return {
                "signal": signal,
                "outputs": []
            }


class Conjunction:
    def __init__(self):
        self.outputs = []
        self.inputs = {}
        self.type = "conjunction"

    def add_input(self, input):
        self.inputs[input] = "l"

    def add_output(self, output):
        self.outputs.append(output)

    def broadcast(self, signal, input):
        self.inputs[input] = signal

        for sig in self.inputs.values():
            if sig == "l":
                return {
                    "signal": "h",
                    "outputs": self.outputs
                }

        return {
            "signal": "l",
            "outputs": self.outputs
        }

data_file = "data.txt"

modules = {}

with open(data_file) as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        m, outputs = line.split(" -> ")

        if m == "broadcaster":
            name = m
            modules[name] = Broadcaster()
        elif m[0] == "%":
            name = m[1:]
            modules[name] = Flipflop()
        else:
            name = m[1:]
            modules[name] = Conjunction()

        for output in outputs.split(", "):
            modules[name].add_output(output)

for m in modules:
    if modules[m].type == "conjunction":
        for k in modules:
            if m != k and m in modules[k].outputs:
                modules[m].add_input(k)

parents = {}
q = deque()

q.append(("l", "broadcaster", "button"))
loops = 0
while 1:
    current_signal = q.popleft()

    if current_signal[0] == "h" and current_signal[1] == "kc":
        if not parents.get(current_signal[2]):
            parents[current_signal[2]] = loops + 1

    if current_signal[1] in modules:
        module_output = modules[current_signal[1]].broadcast(current_signal[0]) if modules[current_signal[1]].type != "conjunction" else modules[current_signal[1]].broadcast(current_signal[0], current_signal[2])

        for o in module_output["outputs"]:
            q.append((module_output["signal"], o, current_signal[1]))

    if not q:
        if len(parents.keys()) == len(modules["kc"].inputs):
            break
        loops += 1
        q.append(("l", "broadcaster", "button"))

print(lcm(*parents.values()))