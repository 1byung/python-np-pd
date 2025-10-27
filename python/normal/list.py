# ============================================
# 리스트 컴프리헨션 단계별 학습
# ============================================

# ============================================
# 예제 1: 기본 (조건 없이 모두 변환)
# ============================================
print("=== 예제 1: 모두 2배로 ===")

# 일반 for문
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    result.append(num * 2)
print("일반 for문:", result)

# 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers]
print("컴프리헨션:", result)

print()


# ============================================
# 예제 2: 조건 추가 (8번 문제와 같은 패턴!)
# ============================================
print("=== 예제 2: 짝수만 선택 ===")

# 일반 for문
numbers = [1, 2, 3, 4, 5, 6]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
print("일반 for문:", result)

# 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5, 6]
result = [num for num in numbers if num % 2 == 0]
print("컴프리헨션:", result)

print()


# ============================================
# 예제 3: 8번 문제 그대로!
# ============================================
print("=== 예제 3: 8번 문제 (50 이상) ===")

# 일반 for문
numbers = [12, 45, 23, 89, 34, 67, 91, 50]
result = []
for number in numbers:
    if number >= 50:
        result.append(number)
print("일반 for문:", result)

# 리스트 컴프리헨션
numbers = [12, 45, 23, 89, 34, 67, 91, 50]
result = [number for number in numbers if number >= 50]
print("컴프리헨션:", result)

print()


# ============================================
# 예제 4: 값을 변환하면서 조건도 적용
# ============================================
print("=== 예제 4: 짝수만 선택해서 제곱 ===")

# 일반 for문
numbers = [1, 2, 3, 4, 5, 6]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num ** 2)  # 제곱
print("일반 for문:", result)

# 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5, 6]
result = [num ** 2 for num in numbers if num % 2 == 0]
print("컴프리헨션:", result)

print()


# ============================================
# 연습 문제: 직접 해보세요!
# ============================================
print("=== 연습 1: 10 이상인 숫자만 선택 ===")
numbers = [5, 12, 3, 18, 7, 25, 9]

# TODO: 일반 for문으로 작성해보세요
result1 = []
# 여기에 코드 작성
for num in numbers:
    if num >= 10:
        result1.append(num)
# TODO: 리스트 컴프리헨션으로 작성해보세요
result2 = [num for num in numbers if num >= 10]  # 한 줄로!


print("일반 for문:", result1)
print("컴프리헨션:", result2)

print()


print("=== 연습 2: 3의 배수만 선택 ===")
numbers = [1, 3, 5, 6, 9, 10, 12, 15]

# TODO: 일반 for문
result1 = []
# 여기에 코드 작성
for num in numbers:
    if num % 3 == 0:
        result1.append(num)

# TODO: 리스트 컴프리헨션
result2 = [num for num in numbers if num % 3 == 0]  # 한 줄로!

print("일반 for문:", result1)
print("컴프리헨션:", result2)


# ============================================
# 공식 정리
# ============================================
print("\n" + "="*50)
print("공식 정리")
print("="*50)
print("""
일반 for문:
    result = []
    for 변수 in 리스트:
        if 조건:
            result.append(변수)

↓ 변환 ↓

리스트 컴프리헨션:
    result = [변수 for 변수 in 리스트 if 조건]

읽는 순서:
    [무엇을  for 어디서  if 언제]
     넣을지      가져올지   조건
""")
