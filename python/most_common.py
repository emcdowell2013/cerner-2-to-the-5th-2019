# cerner_2^5_2019
# Finds the most common element in a list
data = [2,2,1,1,1,2,2]
highest = 0
for i in data:
    if data.count(i) > highest:
        highest = i
print(highest)
