"""
Numpy & Pandas 핵심 파이썬 문법 실습
=======================================
이 파일은 데이터 분석에 자주 사용되는 파이썬 문법을 실습하기 위한 교육용 파일입니다.

📚 학습 방법:
1. 각 파트의 [예제] 코드를 실행하고 이해하기
2. 바로 아래 [연습문제]를 직접 풀어보기
3. 막히면 예제를 다시 참고하기
4. 마지막 종합 연습문제로 실력 점검하기
"""

import numpy as np
import pandas as pd

print("=" * 80)
print("                    Numpy & Pandas 핵심 문법 실습 시작!")
print("=" * 80 + "\n")


# ================================================================================
# 1. 리스트 컴프리헨션 (List Comprehension)
# ================================================================================
print("\n" + "=" * 80)
print("1. 리스트 컴프리헨션")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# 기본 형태: 0~9의 제곱
squares = [x**2 for x in range(10)]
print(f"제곱 리스트: {squares}")

# 조건문 포함: 짝수만
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"짝수만: {even_numbers}")

# 삼항 연산자와 함께: 짝수면 제곱, 홀수면 0
mixed = [x**2 if x % 2 == 0 else 0 for x in range(10)]
print(f"짝수만 제곱: {mixed}")

print("\n[연습문제]")
print("-" * 80)

# TODO 1-1: 1부터 30까지 숫자 중 5의 배수만 리스트로 만들기
multiples_of_5 = [x for x in range(5, 31, 5)]
print(f"5의 배수: {multiples_of_5}")

# TODO 1-2: 1부터 10까지 숫자를 세제곱한 리스트 만들기
cubes = [x ** 3 for x in range(1, 11)]
print(f"세제곱: {cubes}")

# TODO 1-3: 1부터 20까지 숫자 중 홀수는 그대로, 짝수는 0으로 만들기
odd_or_zero = [x if x % 2 != 0 else 0 for x in range(1, 21)]
print(f"홀수 또는 0: {odd_or_zero}")


# ================================================================================
# 2. 슬라이싱 (Slicing)
# ================================================================================
print("\n" + "=" * 80)
print("2. 슬라이싱 [start:end:step]")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"원본: {numbers}")
print(f"[2:7] → {numbers[2:7]}")        # 2~6
print(f"[::2] → {numbers[::2]}")        # 2칸씩
print(f"[::-1] → {numbers[::-1]}")      # 역순
print(f"[:-3] → {numbers[:-3]}")        # 마지막 3개 제외
print(f"[-3:] → {numbers[-3:]}")        # 마지막 3개만

# Numpy 배열 슬라이싱
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print(f"\nNumpy 2D 배열:\n{arr_2d}")
print(f"첫 2행, 2-3열:\n{arr_2d[0:2, 1:3]}")

print("\n[연습문제]")
print("-" * 80)

test_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"연습용 리스트: {test_list}")

# TODO 2-1: 인덱스 3부터 7까지 추출
result_2_1 = test_list[3:8]
print(f"2-1 결과: {result_2_1}")

# TODO 2-2: 3칸씩 건너뛰며 추출
result_2_2 = test_list[::3]
print(f"2-2 결과: {result_2_2}")

# TODO 2-3: 뒤에서 5개 요소만 추출
result_2_3 = test_list[-5:]
print(f"2-3 결과: {result_2_3}")


# ================================================================================
# 3. Boolean 인덱싱 (매우 중요!)
# ================================================================================
print("\n" + "=" * 80)
print("3. Boolean 인덱싱")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# Numpy 예제
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(f"원본 배열: {arr}")
mask = arr > 40
print(f"40보다 큰가? {mask}")
print(f"필터링 결과: {arr[mask]}")

# Pandas 예제
df = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수', '정수진', '최동욱'],
    'age': [25, 30, 35, 28, 32],
    'score': [85, 92, 78, 95, 88],
    'city': ['서울', '부산', '서울', '대구', '서울']
})

print(f"\n원본 데이터:")
print(df)

print(f"\n나이 30 이상:")
print(df[df['age'] >= 30])

print(f"\n서울에 사는 사람:")
print(df[df['city'] == '서울'])

# 여러 조건 (& = and, | = or)
print(f"\n서울 + 점수 85 이상:")
print(df[(df['city'] == '서울') & (df['score'] >= 85)])

print("\n[연습문제]")
print("-" * 80)

# TODO 3-1: 점수가 90점 이상인 사람만 필터링
result_3_1 = df[df['score'] >= 90]
print(f"\n3-1 결과:\n{result_3_1}")

# TODO 3-2: 나이가 28 이하이거나 점수가 90 이상인 사람 (| 사용)
result_3_2 = df[(df['age'] <= 28) | (df['score'] >= 90)]
print(f"\n3-2 결과:\n{result_3_2}")

# TODO 3-3: 서울 또는 대구에 사는 사람 (isin 사용)
result_3_3 = df[df['city'].isin(['서울', '대구'])]
print(f"\n3-3 결과:\n{result_3_3}")


# ================================================================================
# 4. Lambda 함수와 apply() (핵심!)
# ================================================================================
print("\n" + "=" * 80)
print("4. Lambda 함수와 apply()")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# 기본 lambda
square = lambda x: x**2
print(f"5의 제곱: {square(5)}")

# Pandas apply - 단일 컬럼
df['score_doubled'] = df['score'].apply(lambda x: x * 2)
print(f"\n점수 2배:")
print(df[['name', 'score', 'score_doubled']])

# 조건부 처리
df['grade'] = df['score'].apply(
    lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C')
)
print(f"\n등급 부여:")
print(df[['name', 'score', 'grade']])

# 여러 컬럼 활용 (axis=1)
df['info'] = df.apply(
    lambda row: f"{row['name']}({row['age']}세)",
    axis=1
)
print(f"\n정보 조합:")
print(df[['name', 'age', 'info']])

print("\n[연습문제]")
print("-" * 80)

# TODO 4-1: age 컬럼에 10을 더한 새 컬럼 'age_plus_10' 만들기 (apply 사용)
df['age_plus_10'] = df['age'].apply(lambda x: x + 10)
print(f"\n4-1 결과:\n{df[['name', 'age', 'age_plus_10']]}")

# TODO 4-2: 나이가 30 이상이면 '중년', 미만이면 '청년' 컬럼 만들기
df['age_group'] = df['age'].apply(lambda x: '중년' if x >= 30 else '청년')
print(f"\n4-2 결과:\n{df[['name', 'age', 'age_group']]}")

# TODO 4-3: name과 city를 조합해서 "김철수@서울" 형식의 컬럼 만들기 (axis=1 사용)
df['name_city'] = df.apply(lambda x: f"{x['name']}@{x['city']}", axis=1)
print(f"\n4-3 결과:\n{df[['name', 'city', 'name_city']]}")


# ================================================================================
# 5. 딕셔너리 연산과 매핑
# ================================================================================
print("\n" + "=" * 80)
print("5. 딕셔너리 연산과 매핑")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# 매핑 딕셔너리
city_code = {
    '서울': 'SEL',
    '부산': 'PUS',
    '대구': 'DAE',
    '인천': 'ICN'
}

df['city_code'] = df['city'].map(city_code)
print(f"도시 코드 매핑:")
print(df[['name', 'city', 'city_code']])

# get() 메서드
unknown = city_code.get('광주', 'UNKNOWN')
print(f"\n'광주'의 코드: {unknown}")

print("\n[연습문제]")
print("-" * 80)

# TODO 5-1: 등급(A, B, C)을 점수(100, 80, 60)로 변환하는 딕셔너리를 만들고 매핑
grade_score = {'A': 100, 'B': 80, 'C': 60}
df['grade_score'] = df['grade'].map(grade_score)
print(f"\n5-1 결과:\n{df[['name', 'grade', 'grade_score']]}")

# TODO 5-2: get()을 사용해서 딕셔너리에 없는 'D' 등급의 값을 0으로 가져오기
d_score = grade_score.get('D', 0)
print(f"\n5-2 결과: D등급 점수 = {d_score}")


# ================================================================================
# 6. 메서드 체이닝 (Pandas의 꽃!)
# ================================================================================
print("\n" + "=" * 80)
print("6. 메서드 체이닝")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# 여러 작업을 한 번에!
result = (df
    .query('age >= 30')                           # 30세 이상
    .sort_values('score', ascending=False)        # 점수 내림차순
    .reset_index(drop=True)                       # 인덱스 리셋
    [['name', 'age', 'score']]                   # 컬럼 선택
)
print("30세 이상, 점수 높은 순:")
print(result)

print("\n[연습문제]")
print("-" * 80)

# TODO 6-1: 점수가 85점 이상인 사람을 나이 오름차순으로 정렬하고 name, age, score 컬럼만 선택
result_6_1 = (df
    .query('score >= 85')
    .sort_values('age')
    .reset_index(drop=True)
    [['name', 'age', 'score']]
)
print(f"\n6-1 결과:\n{result_6_1}")


# ================================================================================
# 7. enumerate와 zip
# ================================================================================
print("\n" + "=" * 80)
print("7. enumerate와 zip")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# enumerate
fruits = ['사과', '바나나', '오렌지']
print("enumerate:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}번: {fruit}")

# zip
names = ['김철수', '이영희', '박민수']
ages = [25, 30, 28]
cities = ['서울', '부산', '대구']

print("\nzip:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}({age}세) - {city}")

# 리스트 컴프리헨션과 zip
combined = [f"{n}-{a}" for n, a in zip(names, ages)]
print(f"\nzip + 리스트 컴프리헨션: {combined}")

print("\n[연습문제]")
print("-" * 80)

scores = [85, 92, 78]

# TODO 7-1: enumerate를 사용해서 "1위: 92점" 형식으로 출력 (start=1)
print("\n7-1 결과:")
# for idx, score in enumerate(...):
#     print(...)

# TODO 7-2: zip을 사용해서 names, ages, scores를 조합한 리스트 만들기 (예: "김철수/25/85")
# result_7_2 =
# print(f"\n7-2 결과: {result_7_2}")


# ================================================================================
# 8. any()와 all()
# ================================================================================
print("\n" + "=" * 80)
print("8. any()와 all()")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

arr = np.array([1, 2, 3, 4, 5])
print(f"배열: {arr}")
print(f"하나라도 5보다 큰가? {any(arr > 5)}")
print(f"하나라도 3보다 큰가? {any(arr > 3)}")
print(f"모두 0보다 큰가? {all(arr > 0)}")
print(f"모두 3보다 큰가? {all(arr > 3)}")

print("\n[연습문제]")
print("-" * 80)

test_scores = np.array([80, 85, 90, 75, 95])
print(f"시험 점수: {test_scores}")

# TODO 8-1: 하나라도 100점이 있는가?
# result_8_1 =
# print(f"8-1 결과: {result_8_1}")

# TODO 8-2: 모든 점수가 70점 이상인가?
# result_8_2 =
# print(f"8-2 결과: {result_8_2}")

# TODO 8-3: DataFrame에서 모든 사람의 나이가 20 이상인가?
# result_8_3 =
# print(f"8-3 결과: {result_8_3}")


# ================================================================================
# 9. 삼항 연산자와 np.where()
# ================================================================================
print("\n" + "=" * 80)
print("9. 삼항 연산자와 np.where()")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# 기본 삼항 연산자
score_val = 85
result = "합격" if score_val >= 60 else "불합격"
print(f"점수 {score_val}점: {result}")

# np.where()
scores_arr = np.array([85, 92, 55, 78, 45, 90])
results = np.where(scores_arr >= 60, '합격', '불합격')
print(f"\n점수: {scores_arr}")
print(f"결과: {results}")

# 다중 조건
levels = np.where(
    scores_arr >= 90, 'High',
    np.where(scores_arr >= 70, 'Medium', 'Low')
)
print(f"레벨: {levels}")

print("\n[연습문제]")
print("-" * 80)

ages_arr = np.array([15, 25, 35, 45, 55])
print(f"나이 배열: {ages_arr}")

# TODO 9-1: 나이가 30 이상이면 '성인', 미만이면 '청소년' (np.where 사용)
# result_9_1 =
# print(f"9-1 결과: {result_9_1}")

# TODO 9-2: 나이가 50 이상이면 '노년', 30 이상이면 '중년', 미만이면 '청년' (다중 조건)
# result_9_2 =
# print(f"9-2 결과: {result_9_2}")


# ================================================================================
# 10. 집계 함수 & groupby
# ================================================================================
print("\n" + "=" * 80)
print("10. 집계 함수 & groupby")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

# Numpy 집계
arr = np.array([10, 20, 30, 40, 50])
print(f"배열: {arr}")
print(f"합계: {np.sum(arr)}, 평균: {np.mean(arr)}, 최댓값: {np.max(arr)}")

# Pandas 기본 집계
print(f"\nDataFrame 점수 통계:")
print(f"평균: {df['score'].mean():.2f}, 중앙값: {df['score'].median()}")

# groupby
print(f"\n도시별 평균 점수:")
city_avg = df.groupby('city')['score'].mean()
print(city_avg)

# 여러 집계 함수
print(f"\n도시별 상세 통계:")
city_stats = df.groupby('city')['score'].agg(['mean', 'min', 'max'])
print(city_stats)

print("\n[연습문제]")
print("-" * 80)

numbers_arr = np.array([5, 10, 15, 20, 25, 30])

# TODO 10-1: numbers_arr의 표준편차 구하기 (np.std)
# std_dev =
# print(f"10-1 표준편차: {std_dev:.2f}")

# TODO 10-2: DataFrame에서 도시별 평균 나이 구하기
# result_10_2 =
# print(f"\n10-2 도시별 평균 나이:\n{result_10_2}")

# TODO 10-3: 도시별로 나이의 합계와 점수의 평균을 동시에 구하기 (agg 사용)
# result_10_3 = df.groupby('city').agg({
#     'age': ...,
#     'score': ...
# })
# print(f"\n10-3 결과:\n{result_10_3}")


# ================================================================================
# 11. axis 파라미터
# ================================================================================
print("\n" + "=" * 80)
print("11. axis 파라미터 (axis=0: 행↓, axis=1: 열→)")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

df_axis = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
print("원본:")
print(df_axis)
print(f"\naxis=0 (각 열의 합): {df_axis.sum(axis=0).tolist()}")
print(f"axis=1 (각 행의 합): {df_axis.sum(axis=1).tolist()}")

print("\n[연습문제]")
print("-" * 80)

# TODO 11-1: df_axis에서 각 열의 평균 구하기 (axis=0)
# result_11_1 =
# print(f"11-1 각 열의 평균: {result_11_1}")

# TODO 11-2: df_axis에서 각 행의 최댓값 구하기 (axis=1)
# result_11_2 =
# print(f"11-2 각 행의 최댓값: {result_11_2}")


# ================================================================================
# 12. f-string 포맷팅
# ================================================================================
print("\n" + "=" * 80)
print("12. f-string 포맷팅")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

name = "김철수"
age = 25
score = 85.6789

print(f"{name}님은 {age}세, 점수는 {score:.2f}점")
print(f"점수 정수: {score:.0f}, 나이 패딩: {age:03d}")

print("\n[연습문제]")
print("-" * 80)

product = "사과"
price = 1234.567
quantity = 5

# TODO 12-1: "사과 가격: 1234.57원" 형식으로 출력 (소수점 2자리)
# result_12_1 =
# print(f"12-1: {result_12_1}")

# TODO 12-2: "사과 5개 = 6172.84원" 형식으로 출력 (총액 계산, 소수점 2자리)
# result_12_2 =
# print(f"12-2: {result_12_2}")


# ================================================================================
# 13. 결측치 처리
# ================================================================================
print("\n" + "=" * 80)
print("13. 결측치 처리")
print("=" * 80)

print("\n[예제]")
print("-" * 80)

df_missing = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D'],
    'age': [25, np.nan, 30, 35],
    'salary': [3000, 4000, np.nan, 5000]
})
print("원본 (결측치 포함):")
print(df_missing)
print(f"\n결측치 개수:\n{df_missing.isnull().sum()}")

# fillna
df_filled = df_missing.copy()
df_filled['age'] = df_filled['age'].fillna(df_filled['age'].mean())
df_filled['salary'] = df_filled['salary'].fillna(0)
print(f"\nfillna 후:")
print(df_filled)

print("\n[연습문제]")
print("-" * 80)

df_practice = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D'],
    'price': [1000, np.nan, 3000, np.nan],
    'stock': [10, 20, np.nan, 40]
})
print("연습용 데이터:")
print(df_practice)

# TODO 13-1: price의 결측치를 평균값으로 채우기
# df_practice['price'] =
# print(f"\n13-1 결과:\n{df_practice}")

# TODO 13-2: stock의 결측치를 0으로 채우기
# df_practice['stock'] =
# print(f"\n13-2 결과:\n{df_practice}")

# TODO 13-3: 결측치가 있는 행 모두 제거하기 (원본 df_practice 사용)
# df_dropped =
# print(f"\n13-3 결과:\n{df_dropped}")


# ================================================================================
# 종합 실습 문제
# ================================================================================
print("\n\n" + "=" * 80)
print("                         종합 실습 문제")
print("=" * 80)

# 학생 성적 데이터
students_df = pd.DataFrame({
    'student': ['김철수', '이영희', '박민수', '정수진', '최동욱', '한지민', '오승환', '임유진'],
    'math': [85, 92, 78, 95, 88, 72, 90, 85],
    'english': [90, 88, 85, 92, 95, 80, 87, 93],
    'science': [88, 90, 82, 98, 92, 75, 89, 91],
    'class': ['A', 'A', 'B', 'A', 'B', 'B', 'A', 'B']
})

print("\n원본 학생 데이터:")
print(students_df)

print("\n" + "-" * 80)
print("아래 문제들을 순서대로 풀어보세요!")
print("-" * 80)

# TODO 종합-1: 수학 점수가 85점 이상인 학생만 필터링
print("\n[종합-1] 수학 점수 85점 이상인 학생:")
# result_final_1 =
# print(result_final_1)


# TODO 종합-2: 'total'(총점)과 'average'(평균) 컬럼 추가
print("\n[종합-2] 총점과 평균 추가:")
# students_df['total'] =
# students_df['average'] =
# print(students_df[['student', 'total', 'average']])


# TODO 종합-3: 평균이 90 이상이면 'A', 80 이상이면 'B', 나머지 'C' 등급 부여
print("\n[종합-3] 등급 부여:")
# students_df['grade'] =
# print(students_df[['student', 'average', 'grade']])


# TODO 종합-4: 반(class)별 평균 점수 구하기
print("\n[종합-4] 반별 평균 점수:")
# class_avg =
# print(class_avg)


# TODO 종합-5: 메서드 체이닝 - A반이면서 평균 85점 이상인 학생을 평균 내림차순 정렬
print("\n[종합-5] A반, 평균 85+ 학생 (내림차순):")
# result_final_5 = (students_df
#
# )
# print(result_final_5)


# TODO 종합-6: 영어 점수가 90점 이상이고 B반인 학생 찾기 (Boolean 인덱싱)
print("\n[종합-6] 영어 90점 이상 + B반 학생:")
# result_final_6 =
# print(result_final_6)


# TODO 종합-7: 모든 과목이 80점 이상인 학생 찾기 (apply + all 사용)
print("\n[종합-7] 모든 과목 80점 이상인 학생:")
# result_final_7 = students_df[
#     students_df.apply(
#         lambda row: ...,
#         axis=1
#     )
# ]
# print(result_final_7[['student', 'math', 'english', 'science']])


# TODO 종합-8: 각 과목별 최고 점수와 해당 학생 이름 출력
print("\n[종합-8] 각 과목별 최고 점수 학생:")
# for subject in ['math', 'english', 'science']:
#     max_idx = students_df[subject].idxmax()
#     student_name = ...
#     max_score = ...
#     print(f"{subject}: {student_name} ({max_score}점)")


# TODO 종합-9: 총점 상위 3명의 이름과 총점 출력 (sort_values + head)
print("\n[종합-9] 총점 상위 3명:")
# top3 =
# print(top3[['student', 'total']])


# TODO 종합-10: 학생 정보를 "이름(반): 평균점" 형식으로 출력 (apply + f-string)
print("\n[종합-10] 학생 정보 포맷:")
# students_df['formatted'] = students_df.apply(
#     lambda row: ...,
#     axis=1
# )
# for info in students_df['formatted']:
#     print(f"  - {info}")


print("\n" + "=" * 80)
print("                    모든 문제를 풀었다면 축하합니다! 🎉")
print("=" * 80)
print("\n힌트: 막히는 부분이 있다면 위의 각 파트 예제를 다시 참고하세요!")
