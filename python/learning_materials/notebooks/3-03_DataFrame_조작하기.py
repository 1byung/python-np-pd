"""
DataFrame 조작하기
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,4))

df

df.columns = ['a', 'b','c','d']
df.index = pd.date_range('20170701', periods = 6)

df.index

df

df['f'] = [1.0, np.nan, 3.5, 6.1, np.nan, 7.0]
df

# NAN 제거하기
df.dropna(how='any')   # nan이 하나라도 포함된 경우 그 행을 삭제한다.

df.dropna(how='all')   # nan이 행 전체에 있을경우, 그 행을 삭제한다. 아래는 행 전체에 nan이 없으므로 해당되지 않음

# nan 값 대체하기
df.fillna(value=5.0)

# 불리어 마스크로 값 제어하기
df.isnull()

# nan이 있는 행 얻어오기
df.loc[df.isnull()['f'],:]

df

# 인덱스 기준으로 행 삭제하기
pd.to_datetime('20170701')

df.drop(pd.to_datetime('20170701'))

# 인덱스 기준으로 두 개 이상의 행 삭제하기
df.drop([pd.to_datetime('20170701'), pd.to_datetime('20170702')])

# 열 삭제하기
# del df['f']
df.drop('f', axis=1)

df.drop(['b','d'], axis=1)
