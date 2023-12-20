from collections import deque

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

q = deque()

signals = {
    "l": 0,
    "h": 0
}
q.append(("l", "broadcaster", "button"))
loops = 0
while loops < 1000:
    current_signal = q.popleft()
    signals[current_signal[0]] += 1

    if current_signal[1] in modules:
        module_output = modules[current_signal[1]].broadcast(current_signal[0]) if modules[current_signal[1]].type != "conjunction" else modules[current_signal[1]].broadcast(current_signal[0], current_signal[2])

        for o in module_output["outputs"]:
            q.append((module_output["signal"], o, current_signal[1]))

    if not q:
        loops += 1
        still_on = False
        for mods in modules.values():
            if mods.type == "flipflop" and mods.is_on:
                still_on = True
                break
        
        if still_on:
            q.append(("l", "broadcaster", "button"))
        else:
            break

print((1000/loops) * signals["l"] * (1000/loops) * signals["h"])
