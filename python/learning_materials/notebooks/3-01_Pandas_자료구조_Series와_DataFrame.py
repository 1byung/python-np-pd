# pandas의 고유한 자료구조 - Series와 DataFrame
# pandas에서는 Series와 DataFrame을 사용하여 빅 데이터 분석을 할 수 있다.

import pandas as pd
import numpy as np

# 1) Series
# Series는 pd.Series() 함수를 사용하여 정의합니다.

obj = pd.Series([4,7,-5,3])
print(obj)

print(obj.values)
print(obj.index)
print(obj.dtype)
print(obj.shape)

obj2 = pd.Series([4,7,-5,3], index=['d','b','c','a'])
print(obj2)

# Series는 dictionary와 같이 사용할 수도 있다.
sdata = {'Charles ':35000, 'Hyunsuk':16000, 'Hayoung':71000,'Joohee':5000}

obj3 = pd.Series(sdata)
print(obj3)

obj3.name = 'Salary'
obj3.index.name='name'
print(obj3)

# index 변경하기
obj3.index = ['A','B','C','D']
print(obj3)

# 2) DataFrame
# DataFrame은 pd.DataFrame() 함수를 사용하여 정의한다.

data = {"names": ['Hyunsuk','Hyunsuk','Hyunsuk','Charles','Charles'],
        "year": [2014, 2015, 2016, 2015, 2016],
        "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df)

print(df.index)
print(df.columns)
print(df.values)

# DataFrame 관련 함수 혹은 변수 등을 조회하고자 할 경우
# df.까지만 입력하고 TAB 키를 누르면 사용 가능한 모든 변수 및 함수가 표시된다.

# describe 함수: 계산이 가능한 컬럼에 한해서 각 컬럼의 평균, 분산,
# 최솟/최댓값 등 기본 통계량을 산출

df2 = pd.DataFrame(data, columns = ['year','names','points','penalty'],
                  index = ['one','two','three','four','five'])

print(df2)

print(df2.index)
print(df2.columns)
print(df2.values)

# NaN : Not a Number (데이터가 없거나 무한대인 경우)
print(df2.describe())
