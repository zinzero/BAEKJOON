T = int(input())

# number = [[] for _ in range(T)]
number = []
student = []
average = []
sum = 0

for _ in range(T):
    line = input()
    number.append(line)

for i in range(len(number)):
    student.append(number[i].split())

for i in range(T):
    for j in range(int(student[i][0])):
        sum += int(student[i][j])
    average.append(sum / int(student[i][0]))
    sum = 0


# print(number)
# print(student)
print(average)

# for i in range(T):
#     print(student[i][0])

#  귀찮아...

