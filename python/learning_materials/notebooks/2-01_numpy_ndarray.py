"""
numpy는 특히 벡터 및 행렬 연산에 있어 편의성을 제공하는 라이브러리로,
앞으로 사용하게 될 pandas와 시각화 표현에 기반이 되는 라이브러리라고 할 수 있다.

numpy에서는 기본적으로 array(어레이)라는 단위로 데이터를 관리하고,
이에 대한 연산을 수행하게 된다.
"""

import numpy as np

# 1차원 array
data = [6, 7.5, 8, 0, 1]
arr1 = np.array(data)
print(arr1)
print(arr1.shape)

arr = np.array([2,3,4])
print(arr)

# 2차원 array
data2 = [[1,2,3,4],
         [5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.shape)

# zeros(), ones(), arange() 함수 기능
# 0으로 된 array를 만든다.
print(np.zeros((3,6)))

# 1로 된 array를 만든다.
print(np.ones(10))

# 연속된 수로 array를 만든다.
print(np.arange(15))

"""
데이터 타입

numpy에서 사용 가능한 데이터형(dtype) 정리:
- int8, int16, int32, int64: 부호가 있는 정수
- uint8, uint16, uint32, uint64: 부호가 없는 정수
- float16, float32, float64, float128: 실수
- complex64, complex128, complex256: 복소수
- bool: 불리언
- object: Python 오브젝트 형
- string_: 문자열
- unicode_: 유니코드 문자열
"""

print(arr1.dtype)
print(arr2.dtype)

# 데이터 타입 직접 지정하기
arr = np.array([1,2,3,4,5], dtype=np.int64)
print(arr)
print(arr.dtype)

# 기존의 타입을 변경하기 astype()
float_arr = arr.astype(np.float64)
print(float_arr)
print(float_arr.dtype)

"""
array 관련 연산

두 array 간에는 더하기, 빼기, 곱하기, 나누기 등의 연산을 수행할 수 있다.
이 때, 이러한 연산은 두 array 상의 동일한 위치의 성분끼리 이루어지게 되므로,
두 array의 모양이 같아야 계산이 가능하다.

하나의 array와 일반 숫자 간에 연산을 하는 것도 가능한데,
이 경우 해당 숫자와 array 내 모든 성분 간에 해당 연산이 이루어지게 된다.
"""

arr1 = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
arr2 = np.array([[7,8,9],[10,11,12]], dtype=np.float64)
print(arr1)
print(arr2)

# 연산 (+) - 2차원에서 같은 위치의 성분끼리 연산이 된다.
print(arr1 + arr2)

# 각 성분에 일반 숫자를 적용하여 연산하기
print(arr1 * 2)
print(arr1 ** 2)
print(1 / arr1)
