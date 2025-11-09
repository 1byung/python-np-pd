# 변수와 자료형
# 숫자형
age = 25
height = 175.5
price = 1000

# 문자열
name = "홍길동"
city = '서울'

# 불린 (True/False)
is_student = True
is_married = False

# 리스트 (여러 개의 값을 담는 상자)
numbers = [1,2,3,4,5]
names = ["철수", "영희", "민수"]

# 딕셔너리 (키 - 값 쌍으로 저장)
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

# 실습 포인트 : 

# . 변수 이름은 의미있게 짓기
# . 리스트는 [], 딕셔너리는 {}
# . 문자열은 "" 또는 ''

# 2. 연산자

# 산술 연산
a = 10
b = 3

print(a + b)  # 13 (덧셈)
print(a - b)  # 7 (뺄셈)
print(a * b)  # 30 (곱셈)
print(a / b)  # 3.33... (나눗셈)
print(a // b) # 3 (몫)
print(a % b)  # 1 (나머지)

# 비교 연산
print(a > b)  # True
print(a == b) # False
print(a != b) # True

# 3. 조건문 (if문)

# 기본 if문
score = 85

if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
else:
    print("재수강")

# 실전 예제 : 나이에 따른 입장료
age = 15

if age < 8:
    price = 0
    print("무료입장")
elif age < 19:
    price = 5000
    print(f"청소년 요금 : {price}원")
else:
    price = 10000
    print(f"성인 요금 : {price}원")

# 주의사항 : 들여쓰기(Indent)가 매우 중요

# 4. 반복문 (for, while)

# for 반복문 - 정해진 횟수만큼 반복
for i in range(5):
    print(f"{i}번째 반복")

# 리스트 순회
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(f"나는 {fruit}를 좋아해")

# while 반복문 - 조건이 True일 때까지 반복
count = 0
while count < 5:
    print(f"카운트: {count}")
    count += 1

# 실전 예제: 1부터 10까지 합 구하기
total = 0
num = 1

# while 반복문
while num <= 10:
    total += num
    num += 1

print(f"1부터 10까지의 합 : {total}")

# 5. 함수(Function)

# 함수란? 자주 사용하는 코드를 하나로 묶어서 재사용하는 것

# 기본 함수
def greet():
    print("Hello World")

greet() # 함수 호출 

# 매개변수가 있는 함수
def greet_name(name):
    print(f"안녕하세요, {name}님")

greet_name("홍길동")

# 값을 반환하는 함수
def add(a, b):
    return a + b

result = add(3, 5)
print(result) # 8

# 실전 예제 : 평균 계산 함수
def calculate_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return avg

my_scores = [85, 90, 78, 92, 88]
average = calculate_average(my_scores)
print(f"평균 점수: {average}")