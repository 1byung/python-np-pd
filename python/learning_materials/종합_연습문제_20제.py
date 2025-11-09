"""
===============================================================================
데이터 분석 학습 자료 종합 연습문제 (20문제)
===============================================================================

📚 학습 내용 요약:

1단원 - 데이터 분석 기초
- 데이터 분석의 개념과 EDA (탐색적 데이터 분석)
- 빅데이터의 이해

2단원 - NumPy 핵심
- ndarray 생성 및 조작 (zeros, ones, arange)
- 데이터 타입 (dtype, astype)
- 배열 연산 (산술, 브로드캐스팅)
- 인덱싱 & 슬라이싱 (1D, 2D)
- 불리언 인덱싱 (마스크)
- 수학 함수 (square, sqrt, log, maximum, minimum)
- 통계 함수 (sum, mean, std, max, min, argmax, argmin)
- 정렬 (sort) 및 중복 제거 (unique)
- axis 개념 (axis=0: 행방향↓, axis=1: 열방향→)

3단원 - Pandas 핵심
- Series & DataFrame 생성
- 인덱싱: loc (라벨), iloc (위치)
- 불리언 인덱싱
- 결측치 처리 (dropna, fillna, isnull)
- 행/열 추가 및 삭제 (del, drop)
- 집계 함수 (sum, mean, describe)
- 상관계수 (corr)
- 정렬 (sort_index, sort_values)
- 데이터 탐색 (unique, value_counts, isin)
- apply + lambda

===============================================================================
"""

import numpy as np
import pandas as pd

print("=" * 80)
print("                    NumPy & Pandas 종합 연습문제")
print("=" * 80 + "\n")


# ================================================================================
# NumPy 섹션 (문제 1-10)
# ================================================================================
print("\n" + "=" * 80)
print("NumPy 연습문제 (1-10)")
print("=" * 80 + "\n")


# 문제 1: 0부터 20까지의 짝수만 포함하는 numpy array 생성하기
print("문제 1) 0부터 20까지의 짝수만 포함하는 numpy array를 생성하세요.")
arr1 = np.array([x for x in range(21) if x % 2 == 0])
print(f"결과: {arr1}")
print()


# 문제 2: 3x4 크기의 1로 채워진 array를 만들고, 데이터 타입을 int32로 지정하기
print("문제 2) 3x4 크기의 1로 채워진 array를 만들고, 데이터 타입을 int32로 지정하세요.")
arr2 = np.ones((3, 4), dtype=np.int32)
print(f"결과:\n{arr2}")
print(f"데이터 타입: {arr2.dtype}")
print()


# 문제 3: 다음 2D array에서 2행 전체와 3열 전체를 각각 추출하기
print("문제 3) 다음 array에서 2행 전체와 3열 전체를 각각 추출하세요.")
arr3 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
print(f"원본 array:\n{arr3}")
row_2 = arr3[2, :]
col_3 = arr3[:, 3]
print(f"2행: {row_2}")
print(f"3열: {col_3}")
print()


# 문제 4: 1부터 100까지 숫자 중 50보다 큰 숫자만 필터링하기 (불리언 인덱싱)
print("문제 4) 1부터 100까지 숫자 중 50보다 큰 숫자만 필터링하세요.")
arr4 = np.arange(1, 101)
result_4 = arr4[arr4 > 50]
print(f"결과: {result_4}")
print()


# 문제 5: 두 array의 각 위치에서 큰 값만 선택하기
print("문제 5) 두 array에서 각 위치의 큰 값만 선택하여 새 array를 만드세요.")
x = np.array([3, 7, 2, 9, 1])
y = np.array([5, 4, 8, 2, 6])
print(f"x: {x}")
print(f"y: {y}")
result_5 = np.maximum(x, y)
print(f"결과: {result_5}")
print()


# 문제 6: array의 모든 요소를 제곱한 후 평균 구하기
print("문제 6) 다음 array의 모든 요소를 제곱한 후 평균을 구하세요.")
arr6 = np.array([1, 2, 3, 4, 5])
squared = arr6 ** 2
mean_value = squared.mean()
mean_value = (arr6 ** 2).mean()
print(f"제곱 결과: {squared}")
print(f"평균: {mean_value}")
print()


# 문제 7: 2D array에서 각 열의 합계와 각 행의 최댓값 구하기
print("문제 7) 다음 array에서 각 열의 합계와 각 행의 최댓값을 구하세요.")
arr7 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(f"원본:\n{arr7}")
col_sum = arr7.sum(axis=0)
row_max = arr7.max(axis=1)
print(f"각 열의 합계: {col_sum}")
print(f"각 행의 최댓값: {row_max}")
print()


# 문제 8: array를 내림차순으로 정렬하기
print("문제 8) 다음 array를 내림차순으로 정렬하세요.")
arr8 = np.array([3, 7, 1, 9, 2, 8, 4])
sorted_arr = np.sort(arr8)[::-1]
print(f"정렬 결과: {sorted_arr}")
print()


# 문제 9: array에서 중복된 값을 제거하고 오름차순 정렬하기
print("문제 9) 다음 array에서 중복을 제거하고 오름차순으로 정렬하세요.")
arr9 = np.array([5, 2, 8, 2, 9, 5, 1, 8, 3])
unique_sorted = np.unique(arr9)
print(f"결과: {unique_sorted}")
print()


# 문제 10: 0~100 난수 20개를 생성하고, 60 이상인 값의 개수 구하기
print("문제 10) 0~100 난수 20개를 생성하고, 60 이상인 값의 개수를 구하세요.")
np.random.seed(42)  # 재현성을 위한 시드 설정
arr10 = np.random.randint(0, 101, size=20)
print(f"난수 array: {arr10}")
count = (arr10 >= 60).sum()
print(f"60 이상인 값의 개수: {count}")
print()


# ================================================================================
# Pandas 섹션 (문제 11-20)
# ================================================================================
print("\n" + "=" * 80)
print("Pandas 연습문제 (11-20)")
print("=" * 80 + "\n")


# 공통 DataFrame 생성
students = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수', '정수진', '최동욱', '한지민'],
    'math': [85, 92, 78, 95, 88, 72],
    'english': [90, 88, 85, 92, 95, 80],
    'science': [88, 90, 82, 98, 92, 75],
    'class': ['A', 'A', 'B', 'A', 'B', 'B']
})


# 문제 11: DataFrame에서 math 점수가 80점 이상인 학생만 필터링
print("문제 11) math 점수가 80점 이상인 학생만 필터링하세요.")
print("원본 DataFrame:")
print(students)
print()
result_11 = students[students['math'] >= 80]
print(f"결과:\n{result_11}")
print()


# 문제 12: 각 학생의 총점(total)을 계산하여 새 컬럼 추가
print("문제 12) 각 학생의 총점(total)을 계산하여 새 컬럼으로 추가하세요.")
students['total'] = students['math'] + students['english'] + students['science']
print(f"결과:\n{students[['name', 'math', 'english', 'science', 'total']]}")
print()


# 문제 13: loc를 사용하여 '이영희' 학생의 모든 정보 가져오기
print("문제 13) loc를 사용하여 '이영희' 학생의 모든 정보를 가져오세요.")
result_13 = students.loc[students['name'] == '이영희']
print(f"결과:\n{result_13}")
print()


# 문제 14: iloc를 사용하여 첫 3명의 학생의 name, math 컬럼만 가져오기
print("문제 14) iloc를 사용하여 첫 3명의 학생의 name, math 컬럼만 가져오세요.")
result_14 = students.iloc[0:3, [0, 1]]
print(f"결과:\n{result_14}")
print()


# 문제 15: 평균이 90점 이상이면 'A', 80점 이상이면 'B', 나머지 'C' 등급 부여
print("문제 15) 각 학생의 평균을 계산하고, 90점 이상 'A', 80점 이상 'B', 나머지 'C' 등급을 부여하세요.")
students['average'] = students[['math', 'english', 'science']].mean(axis=1)
students['grade'] = students['average'].apply(
    lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C')
)
print(f"결과:\n{students[['name', 'average', 'grade']]}")
print()


# 문제 16: 반(class)별 수학(math) 평균 점수 구하기
print("문제 16) 반(class)별 수학(math) 평균 점수를 구하세요.")
result_16 = students.groupby('class')['math'].mean()
print(f"결과:\n{result_16}")
print()


# 문제 17: 총점 기준으로 내림차순 정렬하고 상위 3명만 선택
print("문제 17) 총점 기준으로 내림차순 정렬하고 상위 3명만 선택하세요.")
result_17 = students.sort_values('total', ascending=False).head(3)
print(f"결과:\n{result_17[['name', 'total']]}")
print()


# 문제 18: 결측치가 포함된 DataFrame 처리하기
print("문제 18) 다음 DataFrame의 결측치를 평균값으로 채우세요.")
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})
print("원본:")
print(df_missing)
print()
df_filled = df_missing.fillna(df_missing.mean())
print(f"결과:\n{df_filled}")
print()


# 문제 19: isin()을 사용하여 특정 학생들만 필터링
print("문제 19) isin()을 사용하여 '김철수', '이영희', '박민수' 학생만 필터링하세요.")
result_19 = students[students['name'].isin(['김철수', '이영희', '박민수'])]
print(f"결과:\n{result_19}")
print()


# 문제 20: apply와 lambda를 사용하여 모든 과목이 85점 이상인 학생 찾기
print("문제 20) apply와 lambda를 사용하여 모든 과목이 85점 이상인 학생을 찾으세요.")
result_20 = students[
    students.apply(
        lambda row: (row['math'] >= 85) & (row['english'] >= 85) & (row['scince'] >= 85),
#       lambda row: all([row['math'] >= 85, row['english'] >= 85, row['scince'] >= 85]),
        axis=1
    )
]
print(f"결과:\n{result_20[['name', 'math', 'english', 'science']]}")
print()


print("=" * 80)
print("                    모든 문제를 풀었다면 축하합니다! 🎉")
print("=" * 80)
print("\n힌트:")
print("- NumPy: np.arange(), np.zeros(), np.ones(), 불리언 인덱싱, np.maximum(), axis 개념")
print("- Pandas: loc[], iloc[], boolean indexing, groupby(), sort_values(), apply()")
