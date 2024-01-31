from collections import deque

class Workflow:
    def __init__(self):
        self.instructions = []
        self.otherwise = ""

    def add_instructions(self, instructions):
        instructions = instructions.split(",")
        self.otherwise = instructions[-1]

        for _, inst in enumerate(instructions[:-1]):
            condition, d = inst.split(":")

            self.instructions.append({
                "cat": condition[0],
                "signal": condition[1],
                "condition": condition[2:],
                "send_to": d
            })

    def run_workflow(self, intervals):
        result = []
        q = deque([intervals])
        for inst in self.instructions:
            if not q:
                return result
            
            current_interval = q.popleft()
            interval = current_interval[inst["cat"]]
            cond = int(inst["condition"])


            if inst["signal"] == ">":
                if interval[0] > cond:
                    current_interval["next_workflow"] = inst["send_to"]
                    result.append(current_interval)
                    return result
                
                elif interval[0] <= cond and interval[1] >= cond:
                    result.append({
                        "x": current_interval["x"],
                        "m": current_interval["m"],
                        "a": current_interval["a"],
                        "s": current_interval["s"],
                        "next_workflow": inst["send_to"],
                    })
                    result[-1][inst["cat"]] = (cond + 1, interval[1])
                    q.append({
                        "x": current_interval["x"],
                        "m": current_interval["m"],
                        "a": current_interval["a"],
                        "s": current_interval["s"],
                        "next_workflow": inst["send_to"],
                    })
                    q[-1][inst["cat"]] = (interval[0], cond)

            else:
                if interval[1] < cond:
                    current_interval["next_workflow"] = inst["send_to"]
                    result.append(current_interval)
                    return result
                
                elif interval[0] <= cond and interval[1] >= cond:
                    result.append({
                        "x": current_interval["x"],
                        "m": current_interval["m"],
                        "a": current_interval["a"],
                        "s": current_interval["s"],
                        "next_workflow": inst["send_to"],
                    })
                    result[-1][inst["cat"]] = (interval[0], cond - 1)
                    q.append({
                        "x": current_interval["x"],
                        "m": current_interval["m"],
                        "a": current_interval["a"],
                        "s": current_interval["s"],
                        "next_workflow": inst["send_to"],
                    })
                    q[-1][inst["cat"]] = (cond, interval[1])
        
        if q:
            q[0]["next_workflow"] = self.otherwise
            result.append(q[0])
        return result


data_file = "data.txt"

workflows = {}

with open(data_file) as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        name, instructions = line.split("{")

        workflows[name] = Workflow()

        workflows[name].add_instructions(instructions[:-1])

q = deque([{
    "x": (1,4000),
    "m": (1,4000),
    "a": (1,4000),
    "s": (1,4000),
    "next_workflow": "in",
}])

combinations = 0
while q:
    cint = q.popleft()

    if cint["next_workflow"] == "A":
        int_comb = 1
        for k in cint.keys():
            if k != "next_workflow":
                int_comb *= (cint[k][1] - cint[k][0] + 1)
        combinations += int_comb
        continue

    if cint["next_workflow"] == "R":
        continue

    next_intervals = workflows[cint["next_workflow"]].run_workflow(cint)

    q.extend(next_intervals)

print(combinations)