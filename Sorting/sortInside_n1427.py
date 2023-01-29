import sys

num = sys.stdin.readline().rstrip()

num_list = list(num)
num_list.sort()
num_list.reverse()
answer = "".join(num_list)

print(answer)
