import sys

N = int(sys.stdin.readline().strip())   # strip() 함수 : 뒤에 개행문자 삭제

words = set()   # 중복 없이 저장

for _ in range(N):
    word = sys.stdin.readline().strip()
    words.add(word)

result = []

for i in words:
    result.append(i)

result.sort()
result.sort(key=len)    # key=len 으로 문자열 길이 순서로 정렬

for j in result:
    print(j)


