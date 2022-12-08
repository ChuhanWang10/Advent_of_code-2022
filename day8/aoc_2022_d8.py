import numpy as np

with open('aoc_2022_inputs/day8_input.txt','r') as f:
    input = f.read().splitlines()
    reshaped_input = []
    for row in input:
        row = list(row)
        reshaped_input.append(row)
forest = np.array(reshaped_input)

height,width = np.shape(forest)
#print([height,width])

# part1
count = 0
for i in range(1,height-1):
    for j in range(1,width-1):
        if forest[i,j] <= max(forest[i,j+1:]) and forest[i,j] <= max(forest[i,0:j]):
            if forest[i,j] <= max(forest[0:i,j]) and forest[i,j] <= max(forest[i+1:,j]):
                count += 1

print("the number of invisible trees:",count)
print("the number of visible trees:",height*width-count)

#part2

def visible_tree_count(center,input):
    # input is a list
    # count how many trees are visible for each direction 
    count = 0
    for item in input:
        count += 1
        if center <= item:
            break
    return count

def Reverse(lst):
    # reverse the list
    return [ele for ele in reversed(lst)]

score = []
for i in range(1,height-1):
    for j in range(1,width-1):
        count_left = visible_tree_count(forest[i,j],Reverse(forest[i,0:j]))
        count_right = visible_tree_count(forest[i,j],forest[i,j+1:]) 
        count_up = visible_tree_count(forest[i,j],Reverse(forest[0:i,j])) 
        count_down = visible_tree_count(forest[i,j],forest[i+1:,j])
        score.append(count_left*count_right*count_up*count_down)

#print(score)
top_score = max(score)
print("highest scenic score:",top_score)
