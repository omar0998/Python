#1. Mean
list1 = [10,12,14,16,18,20,11,13,15,17,19]
mean = sum(list1)/len(list1)
print(f"the mean of the list is: {mean}")

#2. Median
list1.sort()
if len(list1) %2 == 0:
    med1 = list1[len(list1)//2]
    med2 = list1[len(list1)//2-1]
    median = (med1 + med2)/2
else:
    median = list1[len(list1)//2]
print(f"The median is: {median}")

#3. Mode
frequency = {}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(f"The mode is: {mode}")