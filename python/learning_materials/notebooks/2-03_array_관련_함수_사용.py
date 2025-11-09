"""
array 관련 함수 사용

각 성분에 적용되는 함수

numpy에서는 array에 적용할 수 있는 다양한 함수를 제공한다.
이들 중 array의 각 성분에 대하여 특정한 계산을 일괄적으로 수행하기 위한 함수들이 있다.

numpy에서 한 개의 array의 각 성분에 적용되는 함수 정리:
- abs: 각 성분의 절댓값 계산
- sqrt: 각 성분의 제곱근 계산 (array ** 0.5 의 결과와 동일)
- square: 각 성분의 제곱 계산 (array ** 2 의 결과와 동일)
- exp: 각 성분을 무리수 e의 지수로 삼은 값을 계산
- log, log10, log2: 자연로그(밑이 e), 상용로그(밑이 10), 밑이 2인 로그를 계산
- sign: 각 성분의 부호 계산 (+인 경우 1, -인 경우 -1, 0인 경우 0)
- ceil: 각 성분의 소수 첫 번째 자리에서 올림한 값을 계산
- floor: 각 성분의 소수 첫 번째 자리에서 내림한 값을 계산
- isnan: 각 성분이 NaN(Not a Number)인 경우 True를, 그렇지 않은 경우 False를 반환
- isinf: 각 성분이 무한대(infinity)인 경우 True를, 그렇지 않은 경우 False를 반환
- cos, cosh, sin, sinh, tan, tanh: 각 성분에 대한 삼각함수 값을 계산
"""

import numpy as np

arr = np.arange(1, 10)
print(arr)

print(np.square(arr))

print(np.log10(arr))

"""
만약 크기가 같은 두 개의 array x, y가 아래와 같이 주어졌을 때,
np.maximum() 함수를 적용하면 두 array를 동일한 위치의 성분끼리 비교하여
값이 더 큰 성분을 선택, 새로운 array로 리턴한다.
"""

x = np.random.randn(8)
y = np.random.randn(8)

print(x)
print(y)

print(np.maximum(x, y))

"""
numpy에서 두 개의 array의 각 성분에 적용되는 함수 정리:
- add: 두 array에서 동일한 위치의 성분끼리 더한 값을 계산 (arr1 + arr2의 결과와 동일)
- subtract: 두 array에서 동일한 위치의 성분끼리 뺀 값을 계산 (arr1 - arr2의 결과와 동일)
- multiply: 두 array에서 동일한 위치의 성분끼리 곱한 값을 계산 (arr1 * arr2의 결과와 동일)
- divide: 두 array에서 동일한 위치의 성분끼리 나눈 값을 계산 (arr1 / arr2의 결과와 동일)
- maximum: 두 array에서 동일한 위치의 성분끼리 비교하여 둘 중 최댓값을 반환
- minimum: 두 array에서 동일한 위치의 성분끼리 비교하여 둘 중 최솟값을 반환
"""

"""
통계 함수

numpy의 array에 적용되는 통계 함수 정리:
- sum: 전체 성분의 합을 계산
- mean: 전체 성분의 평균을 계산
- std, var: 전체 성분의 표준편차, 분산을 계산
- min, max: 전체 성분의 최솟값, 최댓값을 계산
- argmin, argmax: 전체 성분의 최솟값, 최댓값이 위치한 인덱스를 반환
- cumsum: 맨 첫번째 성분부터 각 성분까지의 누적합을 계산 (0에서부터 계속 더해짐)
- cumprod: 맨 첫번째 성분부터 각 성분까지의 누적곱을 계산 (1에서부터 계속 곱해짐)
"""

arr = np.random.randn(5, 4)
print(arr)

print(arr.sum())

print(arr.mean())

print(arr.sum(axis=0))

print(arr.sum(axis=1))

print(arr > 0)

print((arr > 0).sum())

"""
정렬 함수 및 기타 함수
"""

arr = np.random.randn(8)
print(arr)

print(np.sort(arr))

print(np.sort(arr)[::-1])

arr = np.random.randn(5, 3)
print(arr)

print(np.sort(arr, axis=0))

print(np.sort(arr, axis=1))

"""
만약 길이가 아주 긴 large_arr array가 정의되어 있을 때,
해당 array 상에서 상위 5%에 위치하는 값은 다음과 같이 찾아낼 수 있다.
"""

large_arr = np.random.randn(150)
print(large_arr)

print(np.sort(large_arr)[::-1])

print(np.sort(large_arr)[::-1][int(0.05 * len(large_arr))])

"""
large_arr을 먼저 오름차순으로 정렬한 뒤, int(0.05 * len(large_arr))을 통해
상위 5%에 해당하는 인덱스를 계산한 후, 이를 사용하여 정렬 결과에 대한
인덱싱을 수행하는 과정으로 진행.

마지막으로, 중복된 성분을 포함하고 있는 array에 대하여,
np.unique() 함수를 사용하면 중복된 값을 제외한 유니크한 값만을 추출할 수 있다.
"""

# 중복된 값 제거하기 - unique()
names = np.array(['charles', 'hyunsuk', 'charles', 'hayoung', 'hyunsuk', 'joohee', 'joohee'])
ints = np.array([3, 3, 3, 4, 4, 1, 1, 2, 5, 5, 6, 8])

print(np.unique(names))

print(np.unique(ints))
