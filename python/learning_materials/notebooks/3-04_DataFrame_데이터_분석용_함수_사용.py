# DataFrame 데이터 분석용 함수 사용

import pandas as pd
import numpy as np

data = [[1.40, np.nan],
       [7.10,-4.5],
       [np.nan, np.nan],
       [0.75,-1.3]]

df = pd.DataFrame(data, columns = ['one', 'two'], index = ['a','b','c','d'])

df

# 행방향으로 열의 합을 계산  (nan은 배제하고 계산됨)
df.sum(axis=0)

# 열방향으로 각 행의 합을 계산
df.sum(axis=1)

# 특정 열 또는 행의 값 계산

df['one'].sum()

df.loc['b'].sum()

df.mean(axis=0)['two']  # == df['two].mean()

df.mean(axis=1, skipna=False)

df

# 상관계수 구하기

one_mean = df.mean(axis=0)['one']
two_min = df.min(axis=0)['two']

df['one'] = df['one'].fillna(value=one_mean)
df['two'] = df['two'].fillna(value=two_min)

df

df2 = pd.DataFrame(np.random.randn(6,4),
                  columns = ['a','b','c','d'],
                  index = pd.date_range('20171201', periods = 6))
df2

#a열과 b열의 상관계수 산출하기 (피어슨상관계수로 계산)
df2['a'].corr(df2['b'])

df2.corr()

# 정렬 및 기타 함수

# 불규칙하게 데이터 섞기
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=['d','c','a','b'])

df2

# index 기준으로 오름차순 정렬
df2.sort_index(axis=0)

# 컬럼 기준으로 오름차순 정렬
df2.sort_index(axis=1)

# 인덱스 기준으로 내림차순 정렬
df2.sort_index(axis=0, ascending=False)

# 컬럼 기준으로 내림차순 정렬
df2.sort_index(axis=1, ascending=False)

# value 기준으로 오름차순 정렬
df2.sort_values(by='a')

# value 기준으로 내림차순 정렬
df2.sort_values(by='b', ascending=False)

df2['e'] = np.random.randint(0,6, size=6)
df2['f'] = ['alpha', 'beta', 'gamma', 'gamma', 'alpha', 'gamma']

df2

# 오름차순 정렬
df2.sort_values(by=['e','f'])

# 내림차순 정렬
df2.sort_values(by=['e','f'], ascending=False)

df2['f'].unique()

df2['f'].value_counts()

df2['f'].isin(['alpha', 'gamma'])  # alpha, gamma 가 있는지 확인

df2.loc[df2['f'].isin(['alpha', 'gamma']), :]   # alpha, gamma가 있는 행의 전체 값

df3 = pd.DataFrame(np.random.randn(4,3),
                     index = ['Seoul', 'Incheon', 'Busan', 'Daegu'],
                     columns = ['b','d','e'])

df3

func = lambda x: x.max() - x.min()   # x.max : 행 또는 열의 최대값, x.min : 행 또는 열의 최소값

df3.apply(func, axis=0)  # 행방향으로 열 별로 값을 계산

df3.apply(func, axis=1) # 열방향으로 행 별로 값을 계산
