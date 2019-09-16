# cerner_2^5_2019
# Finds the most common element in a list
data = [2,2,1,1,1,2,2,3,2,6,7,7,7,4,4,3,5,5,5,5,5,5,9,9,9,9,0,5,5,5,7,8,2,2,3,3,4,4]
highest = 0
for i in data:
    if data.count(i) > data.count(highest):
        highest = i
print(highest)
