# 문제 1 : 두 숫자를 변수에 저장하고, 사칙연산(+ - * /)의 결과를 모두 출력하세요.
num1 = 10
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# 문제 2 : 당신의 이름, 나이, 사는 도시를 변수에 저장하고, "제 이름은 [이름]이고, [나이]살이며, [도시]에 살고 있습니다." 형식으로 출력하세요.
profile = {
    "name" : "김태윤",
    "age" : 25,
    "city" : "서울" 
}
    

print(f"제 이름은 {profile['name']}이고, {profile['age']}살 이며, {profile['city']}에 살고 있습니다.")

# 문제 3 : 리스트에 좋아하는 과일 5개를 저장하고, 리스트의 길이(개수)만큼 반복하여 과일을 순차적으로 출력하세요.
fruits = ["사과", "바나나", "포도", "딸기", "배"]

for fruit in fruits:
    print(fruit)

# 문제 4: 사용자의 나이를 변수에 저장하고, 다음 조건에 따라 출력하세요.
# 19세 미만: "미성년자입니다"
# 19세 이상 65세 미만: "성인입니다"
# 65세 이상: "노인입니다"

age = 25
if age < 19:
    print("미성년자입니다.")
elif age >= 19 and age < 65:
    print("성인입니다.")
else:
    print("노인입니다.")

# 문제 5: 시험 점수를 변수에 저장하고, 다음 조건으로 학점을 출력하세요.
# 90점 이상: "A"
# 80점 이상: "B"
# 70점 이상: "C"
# 60점 이상: "D"
# 60점 미만: "F"
score = 100
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# 문제 6: 숫자 하나를 변수에 저장하고, 짝수인지 홀수인지 판별하여 출력하세요. (힌트: % 연산자 사용)
num3 = 10
if num3 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 문제 7: 1부터 100까지의 숫자 중에서 3의 배수만 출력하세요.
# 공식: range(시작, 끝, 증가값)
# 시작: 포함됨
# 끝: 포함 안됨! (미만)
# 증가값: 생략하면 1
# range(10)        # 0, 1, 2, ..., 9 (0부터 9까지)
# range(1, 11)     # 1, 2, 3, ..., 10 (1부터 10까지)
# range(0, 10, 2)  # 0, 2, 4, 6, 8 (0부터 10 미만, 2씩 증가)
# range(10, 0, -1) # 10, 9, 8, ..., 1 (10부터 1까지 역순)

for num4 in range(3, 101, 3): # 3부터 100까지 3씩 증가
    print(num4)

# 문제 8: 리스트 numbers = [12, 45, 23, 89, 34, 67, 91, 50]에서 50 이상인 숫자만 출력하세요. 
numbers = [12, 45, 23, 89, 34, 67, 91, 50]
for num in numbers:
    if num >= 50:
        print(num)

# numbers = [12, 45, 23, 89, 34, 67, 91, 50]
# result = [num for num in numbers if num >= 50]
# print(result)  # [89, 67, 91, 50]

numbers = [12, 45, 23, 89, 34, 67, 91, 50]
result = list(filter(lambda x: x >= 50, numbers))
print(result)

# 문제 9: 구구단 5단을 출력하세요.
# 예상 출력:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 9 = 45
# result = [print("5 x ", x, " = ", 5 * x) for x in range(1, 10)]
# for x in range(1, 10):
#     print(f"5 x {x} = {5 * x}")
for x in range(1, 10):
    print(f"5 x {x} = {5 * x}")


# 문제 10: 1부터 50까지의 숫자 중에서 5의 배수의 합을 구하세요. (예: 5 + 10 + 15 + ... + 50)
total = 0

for i in range(5, 51, 5):
    total += i
print(total)

# total = sum(range(5, 51, 5))
# print(total)


# 문제 11: 두 숫자를 받아서 큰 수를 반환하는 함수 find_max(a, b)를 만드세요.
def find_max(a, b):
    if a < b:
        return b
    else:
        return a
    
# def find_max(a, b)
#   return a if a > b else b

# 문제 12: 리스트를 받아서 리스트 안의 모든 숫자의 합을 반환하는 함수 sum_list(numbers)를 만드세요. (힌트: sum() 내장 함수 사용 금지! 반복문으로 직접 구현)
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 문제 13: 이름과 나이를 받아서 "안녕하세요, [이름]님! [나이]살이시군요."를 출력하는 함수 introduce(name, age)를 만드세요.
def introduce(name, age):
    print(f"[{name}]님! [{age}]살이시군요.")

# 문제 14: 숫자를 받아서 그 숫자가 소수(prime number)인지 판별하는 함수 is_prime(n)을 만드세요.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# 소수: 1과 자기 자신으로만 나누어떨어지는 수 (예: 2, 3, 5, 7, 11, 13...)
# True 또는 False 반환

# 문제 15: 온도 변환 프로그램을 만드세요.
# 섭씨를 받아서 화씨로 변환하는 함수 celsius_to_fahrenheit(c)
# 화씨를 받아서 섭씨로 변환하는 함수 fahrenheit_to_celsius(f)
# 공식: F = C × 9/5 + 32
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# 문제 16: 리스트 scores = [85, 92, 78, 90, 88, 76, 95, 89]를 받아서 다음을 계산하는 프로그램을 만드세요.
# 평균 점수
# 최고 점수
# 최저 점수
# 90점 이상인 점수의 개수
scores = [85, 92, 78, 90, 88, 76, 95, 89]
total = sum(scores)
avg = total / len(scores)
best_score = scores[0]
for score in scores:
    if score > best_score:
        best_score = score
# best_score = max(scores) 이건 max 내장함수
worst_score = scores[0]
for score in scores:
    if score < worst_score:
        worst_score = score
# worst_score = min(scores) 이건 min 내장함수
count = len([score for score in scores if score >= 90])
print(f"평균점수 : {avg}, 최고점수 : {best_score}, 최저점수 : {worst_score}, 90점 이상인 점수의 개수 : {count}")


# 문제 17: 구구단 2단부터 9단까지 모두 출력하는 프로그램을 만드세요. (이중 반복문 사용)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")

# 문제 18: 리스트에서 중복을 제거하는 함수 remove_duplicates(lst)를 만드세요.
# # 예시
# numbers = [1, 2, 3, 2, 4, 1, 5, 3]
# 결과: [1, 2, 3, 4, 5]
def remove_duplicates(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

# def remove_duplicates(lst):
#     return list(set(lst))  # set은 자동으로 중복 제거

# 문제 19: 입력받은 문자열이 회문(palindrome)인지 확인하는 함수 is_palindrome(text)를 만드세요.
# 회문: 앞에서 읽으나 뒤에서 읽으나 같은 문자열 (예: "level", "noon", "racecar")

def is_palindrome(text):
    return text == text[::-1]

# text[::-1] - 문자열을 뒤집기
# "level"[::-1] → "level" (같음!)
# "hello"[::-1] → "olleh" (다름!)

# 문제 20: 1부터 N까지의 숫자 중에서:
# 3의 배수이면 "Fizz"
# 5의 배수이면 "Buzz"
# 3과 5의 공배수이면 "FizzBuzz"
# 그 외에는 숫자 그대로 출력
# 함수 fizzbuzz(n)을 만드세요. (유명한 코딩 테스트 문제!)
def fizzbuzz(n):
    for x in range(1, n+1):
        if x % 15 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)