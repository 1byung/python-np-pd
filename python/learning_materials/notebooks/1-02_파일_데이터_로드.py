# %matplotlib inline
import pandas as pd
import numpy as np

# numpy로 파일 읽어오기
# data = np.loadtxt('./data/movielens/ratings.csv', delimiter = '::', dtype=np.int64)
data = np.genfromtxt('./data/movielens/ratings_.dat', delimiter = '::', dtype=np.int64)
# delimiter='::', dtype=int, comments='%', encoding='latin1'

data

# 5행까지 확인해보기
data[:6, :]

data.shape

# pandas 로 파일 읽어오기
names = pd.read_csv("data/NationalNames.csv", header=0, names=['id','name','year','sex','births'])

names.head()

names.count()

names.shape

names.tail()

"""
문제) 년도 별 남자와 여자의 총 합 구하기
"""

total_birth = names.pivot_table('births', index ='year', columns = 'sex', aggfunc = sum)

total_birth.head(10)

total_birth.plot(title='Total births by sex and year')

"""
Python 데이터 분석 라이브러리

1) numpy

numpy는 주요한 Python 데이터 분석 라이브러리들의 기본 베이스가 되는 라이브러리이다.
numpy는 특히 벡터(vector) 및 행렬(array) 연산에 있어 엄청난 편의성을 제공하는 라이브러리이다.

데이터 분석을 하는 데 직접적으로 많이 사용하지는 않겠지만, 추후 많이 사용하게 될
pandas와 matplotlib의 기반이 되는 라이브러리라고 할 수 있다.

2) pandas

pandas는 고유하게 정의한 Series 및 DataFrame 등의 자료구조를 활용하여,
빅 데이터 분석에 있어 높은 수준의 퍼포먼스를 가능하게 하는 라이브러리이다.

3) matplotlib, seaborn

matplotlib, seaborn은 데이터 시각화를 위한 라이브러리이다. 엑셀에서 차트를 그릴
경우 데이터의 양이 조금만 많아지더라도 엄청나게 버벅이는데, matplotlib 등을 사용하면
데이터 분석 결과에 대한 시각화를 빠르고 깔끔하게 수행할 수 있다.
"""
