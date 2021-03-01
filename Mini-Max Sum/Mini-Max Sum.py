import itertools
# 효율적인 루핑을 위한 이터레이터를 만드는 함수

arr=[1,2,3,4,5]
ans = []
for i in itertools.combinations(arr, 4):
    ans.append(sum(i))
print(min(ans), max(ans))