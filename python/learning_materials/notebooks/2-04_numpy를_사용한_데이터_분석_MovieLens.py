import numpy as np

# Load MovieLens ratings data
data = np.genfromtxt('./data/movielens/ratings.dat', delimiter = '::', dtype=np.int64)

"""
데이터 컬럼 내용
user_id :: item :: rating :: timestamp
"""

# Display first 6 rows
print(data[:6, :])

# Check data shape
print(data.shape)

"""
문제) 전체 평균 평점 계산하기
"""

# 데이터 컬럼 내용
# user_id :: item :: rating :: timestamp

# Calculate overall mean rating
mean_rating_total = data[:, 2].mean()
print(mean_rating_total)

"""
문제) 각 사용자 별 평균 평점 계산하기
"""

# Extract unique user IDs
user_ids = np.unique(data[:,0])
print(user_ids[:10])
print(user_ids.shape)

# Calculate mean rating per user
mean_rating_by_user_list = []

for user_id in user_ids:
    data_for_user = data[data[:,0] == user_id, :]
    mean_rating_for_user = data_for_user[:, 2].mean()
    mean_rating_by_user_list.append([user_id, mean_rating_for_user])

print(data_for_user[:10])
print(mean_rating_by_user_list[:10])

# Convert to NumPy array
mean_rating_by_user_list_array = np.array(mean_rating_by_user_list, dtype=np.float64)
print(mean_rating_by_user_list_array.shape)

"""
파일에 writing하기
"""

# Save to CSV file
np.savetxt("./data/movielens/mean_rating_by_user.csv",
           mean_rating_by_user_list_array,
           fmt="%.3f",
           delimiter=',')
