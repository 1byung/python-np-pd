"""
array 인덱싱 이해하기

기본 인덱싱
"""

import numpy as np

arr = np.arange(10)

print(arr)
# Output: [0 1 2 3 4 5 6 7 8 9]

print(arr[5])
# Output: 5

print(arr[5:8])
# Output: [5 6 7]

arr[5:8] = 12

print(arr)
# Output: [ 0  1  2  3  4 12 12 12  8  9]

print(arr[:])
# Output: [ 0  1  2  3  4 12 12 12  8  9]

arr[5:8] = [5,6,7]

print(arr)
# Output: [0 1 2 3 4 5 6 7 8 9]

"""
2차원 array
"""

arr2 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
               [13,14,15,16]])

# 2행의 전체값 가져오기
print(arr2[2, :])
# Output: [ 9 10 11 12]

# 1행~2행의 전체값 가져오기
print(arr2[1:3, :])
# Output: [[ 5  6  7  8] [ 9 10 11 12]]

# 전체 행을 가져오되, 마지막 열 값만을 가져와라
print(arr2[:,3])
# Output: [ 4  8 12 16]

# 3행의 2열값만 가져와라
print(arr2[3,2])
# Output: 15

# 0~1행까지 1~2열까지의 값만 가져와라
print(arr2[:2, 1:3])
# Output: [[2 3] [6 7]]

print(arr2)

"""
불리언 인덱싱
"""

names = np.array(['Charles','Hyunsuk', 'Hayoung', 'Charles', 'Hayoung', 'Hyunsuk', 'Hyunsuk'])
data = np.random.randn(7,4)

print(names)

print(data)

# Charles 값만 확인하기
print(names == 'Charles')
# Output: [ True False False  True False False False]

# Charles의 마스크를 이용하여 다른 array를 인덱싱하기
print(data[names == 'Charles', :])

print(data[names == 'Hyunsuk', :])

# Charles 또는 Hyunsuk의 마스크를 이용하여 array 인덱싱하기
print(data[(names == 'Charles') | (names == 'Hyunsuk'),:])

# 조건부 마스크
print(data[:, 3] < 0)

data[data[:,3] < 0, :] = 0

print(data)
