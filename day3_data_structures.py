number = list(map(int,input("enter no. : ").split()))

print("sum : ", sum(number))
print("max : ", max(number))
print("min : ", min(number))

frequency = {}

for num in number:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)

reverse = []

for i in range(len(number) - 1, -1, -1):
    reverse.append(number[i])

print("Reversed list:", reverse)




