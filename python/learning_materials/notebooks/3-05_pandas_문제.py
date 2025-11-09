# Pandas Data Analysis Script

import pandas as pd
import numpy as np

# pandas를 사용한 데이터 분석
# 파일 읽기
# 대부분의 데이터셋은 열과 열을 구분하기 위한 구분자로 특정한 문자를 사용한다.
# 구분자는 보통 콤마 ','를 많이 쓰는데, 콤마를 구분자로 사용한 파일을
# 특별히 'CSV(comma-separated values) 파일'이라고 부른다.

pd = pd.read_csv('data/loan.csv', sep=',')

# Lending Club Loan dataset 분석하기
# Lending Club Loan dataset의 주요 컬럼 요약
# • loan_amnt: 대출자의 대출 총액
# • funded_amnt: 해당 대출을 위해 모금된 총액
# • issue_d: 대출을 위한 기금이 모금된 월
# • loan_status: 대출의 현재 상태
# • title: 대출자에 의해 제공된 대출 항목
# • purpose: 대출자에 의해 제공된 대출 목적
# • emp_length: 대출자의 재직 기간
# • grade: LC assigned loan grade
# • int_rate: 대출 이자율
# • term: 대출 상품의 기간 (36-month vs. 60-month)
#
# 불량 상태(bad status): "Charged Off", "Default",
# "Does not meet the credit policy. Status:Charged Off",
# "In Grace Period", "Default Receiver", "Late (16-30 days)",
# "Late (31-120 days)"

pd.head(10)
pd.shape
pd.columns

# 필요한 컬럼만 가져오기
df2 = pd[['loan_amnt', 'loan_status', 'grade', 'int_rate', 'term']]

df2.head(10)
df2.tail()
df2['loan_status'].unique()
df2['grade'].unique()
df2['term'].unique()
df2.shape

# nan 제거하기
# how = 'any' 는 nan이 있는 행은 모두 삭제
# how = 'all' 은 행 전체에 nan이 있는 경우에만 행 삭제
df2 = df2.dropna(how='any')

df2.shape

"""
30개월 / 60개월 두 가지 대출 상품을 운영
문제) '36개월 대출'과 '60개월 대출'의 대출 총액 파악
"""

"""
문제) 각 대출 상태(불량/우량)에 따른 대출 등급 분포 파악
"""

"""
대출 총액과 대출 이자율 간의 상관관계 파악
"""

"""
파일쓰기
"""
