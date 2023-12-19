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
                "condition": condition,
                "send_to": d
            })

    def run_workflow(self, x, m, a, s):
        for inst in self.instructions:
            cond_state = eval(inst["condition"])

            if cond_state:
                return inst["send_to"]
            
        return self.otherwise

data_file = "data.txt"

workflows = {}
parts = []

with open(data_file) as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        name, instructions = line.split("{")

        workflows[name] = Workflow()

        workflows[name].add_instructions(instructions[:-1])

    while 1:
        line = f.readline()

        if not line:
            break

        part_arr = line.strip()[1:-1].split(",")

        new_part = []

        for p in part_arr:
            new_part.append(int(p[2:]))
        
        parts.append(new_part)

part_sum = 0
for part in parts:
    current_workflow = workflows["in"]

    while 1:
        next_workflow = current_workflow.run_workflow(part[0], part[1], part[2], part[3])

        if next_workflow == "A":
            part_sum += part[0] + part[1] + part[2] + part[3]
            break

        if next_workflow == "R":
            break

        current_workflow = workflows[next_workflow]


print(part_sum)