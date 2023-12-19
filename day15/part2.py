data_file = "data.txt"

def hash_func(label):
    current_val = 0
    for c in label:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val

with open(data_file) as f:
    data = f.readline().strip().split(",")


total = 0
hashtable = {}
boxes = {}

for step in data:
    if "=" in step:
        step_arr = step.split("=")
        label = step_arr[0]
        focal_length = step_arr[1]

        if not hashtable.get(label):
            new_box_id = hash_func(label)
            hashtable[label] = new_box_id
        
        box_id = hashtable[label]
        if not boxes.get(box_id):
            boxes[box_id] = []

        has_lens = False

        for l in boxes[box_id]:
            if l[0] == label:
                l[1] = int(focal_length)
                has_lens = True
                break
        
        if not has_lens:
            boxes[box_id].append([label, int(focal_length)])
    
    else:
        label = step[:-1]

        if not hashtable.get(label):
            new_box_id = hash_func(label)
            hashtable[label] = new_box_id
        
        box_id = hashtable[label]

        if boxes.get(box_id):
            boxes[box_id] = [b for b in boxes[box_id] if b[0] != label]
 
for id in boxes:
    for idx, l in enumerate(boxes[id]):
        total += (id + 1) * (idx + 1) * l[1]
 
print(boxes)
print(total)