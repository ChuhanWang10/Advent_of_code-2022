with open('aoc_2022_inputs/day6_input.txt', 'r') as f:
    data = f.read()
    data = list(data)

left = 0
right = 0
window = dict()

# part 1
while right < len(data):
    if data[right] not in window:
        window[data[right]] = 1
    else:
        window[data[right]] += 1
    
    while window[data[right]] > 1:
        window[data[left]] -= 1
        left += 1
    
    if right - left == 4: #change from 4 to 14 for part 2
        break

    right += 1

print("the number of characters to be processed:",right)

    

