# ============================================
# NBA 경기 결과 예측 프로젝트
# ============================================
# 머신러닝으로 NBA 경기 승패 예측하기!

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

print("="*60)
print("NBA 경기 결과 예측 시스템")
print("="*60)
print()

# ============================================
# 1단계: 데이터 준비
# ============================================
print("[1단계] 데이터 로드")
print("-"*60)

# 실제 NBA 스타일 경기 데이터 생성
# (나중에 실제 데이터로 교체 가능)
np.random.seed(42)

# 팀 이름
teams = ['Lakers', 'Warriors', 'Celtics', 'Nets', 'Heat',
         'Bucks', 'Suns', 'Clippers', 'Nuggets', 'Mavericks']

# 100경기 시뮬레이션
num_games = 100

data = {
    'home_team': np.random.choice(teams, num_games),
    'away_team': np.random.choice(teams, num_games),
    'home_team_rating': np.random.randint(75, 95, num_games),  # 팀 종합 능력치
    'away_team_rating': np.random.randint(75, 95, num_games),
    'home_team_wins_last_10': np.random.randint(3, 10, num_games),  # 최근 10경기 승수
    'away_team_wins_last_10': np.random.randint(3, 10, num_games),
    'home_team_avg_points': np.random.randint(100, 120, num_games),  # 평균 득점
    'away_team_avg_points': np.random.randint(100, 120, num_games),
    'home_advantage': 1,  # 홈 어드밴티지 (항상 1)
}

# 승패 결정 (간단한 로직: 능력치 + 최근성적 + 홈어드밴티지)
home_score = (data['home_team_rating'] * 0.5 +
              data['home_team_wins_last_10'] * 2 +
              data['home_advantage'] * 5 +
              np.random.randint(-10, 10, num_games))

away_score = (data['away_team_rating'] * 0.5 +
              data['away_team_wins_last_10'] * 2 +
              np.random.randint(-10, 10, num_games))

data['home_team_win'] = (home_score > away_score).astype(int)

df = pd.DataFrame(data)

print("데이터 샘플:")
print(df.head(10))
print(f"\n총 경기 수: {len(df)}")
print(f"홈팀 승리: {df['home_team_win'].sum()}경기")
print(f"원정팀 승리: {len(df) - df['home_team_win'].sum()}경기")
print()

# ============================================
# 2단계: 데이터 분석 (EDA)
# ============================================
print("[2단계] 데이터 분석")
print("-"*60)

# 홈 어드밴티지 분석
home_win_rate = df['home_team_win'].mean() * 100
print(f"홈팀 승률: {home_win_rate:.1f}%")
print(f"원정팀 승률: {100 - home_win_rate:.1f}%")
print()

# 능력치 차이와 승률 관계
df['rating_diff'] = df['home_team_rating'] - df['away_team_rating']
df['recent_form_diff'] = df['home_team_wins_last_10'] - df['away_team_wins_last_10']

print("능력치 차이별 홈팀 승률:")
for diff_range in [(-20, -10), (-10, 0), (0, 10), (10, 20)]:
    mask = (df['rating_diff'] >= diff_range[0]) & (df['rating_diff'] < diff_range[1])
    if mask.sum() > 0:
        win_rate = df[mask]['home_team_win'].mean() * 100
        print(f"  능력치 차이 {diff_range}: {win_rate:.1f}% ({mask.sum()}경기)")
print()

# ============================================
# 3단계: 특성(Feature) 준비
# ============================================
print("[3단계] 머신러닝 특성 준비")
print("-"*60)

# 예측에 사용할 특성 선택
features = [
    'home_team_rating',
    'away_team_rating',
    'home_team_wins_last_10',
    'away_team_wins_last_10',
    'home_team_avg_points',
    'away_team_avg_points',
    'home_advantage',
    'rating_diff',
    'recent_form_diff'
]

X = df[features]
y = df['home_team_win']

print(f"특성 개수: {len(features)}")
print(f"사용 특성: {features}")
print(f"\n특성 데이터 샘플:\n{X.head()}")
print()

# ============================================
# 4단계: 데이터 분할 (훈련/테스트)
# ============================================
print("[4단계] 데이터 분할")
print("-"*60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"전체 데이터: {len(df)}경기")
print(f"훈련 데이터: {len(X_train)}경기")
print(f"테스트 데이터: {len(X_test)}경기")
print()

# ============================================
# 5단계: 머신러닝 모델 학습!
# ============================================
print("[5단계] 머신러닝 모델 학습")
print("-"*60)

# Random Forest 모델 생성
model = RandomForestClassifier(
    n_estimators=100,  # 결정 트리 100개
    random_state=42,
    max_depth=10
)

print("모델: Random Forest (랜덤 포레스트)")
print("학습 시작...")

# 모델 학습!
model.fit(X_train, y_train)

print("[완료] 학습 완료!")
print()

# ============================================
# 6단계: 모델 평가
# ============================================
print("[6단계] 모델 성능 평가")
print("-"*60)

# 예측
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# 정확도
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f"훈련 데이터 정확도: {train_accuracy*100:.1f}%")
print(f"테스트 데이터 정확도: {test_accuracy*100:.1f}%")
print()

# 상세 리포트
print("상세 분류 리포트:")
print(classification_report(y_test, y_pred_test,
                          target_names=['원정팀 승', '홈팀 승']))

# 혼동 행렬
print("혼동 행렬:")
cm = confusion_matrix(y_test, y_pred_test)
print(cm)
print()

# 특성 중요도
print("특성 중요도 (어떤 요소가 승패에 영향을 미칠까?):")
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

for idx, row in feature_importance.iterrows():
    print(f"  {row['feature']:25s}: {row['importance']*100:5.1f}%")
print()

# ============================================
# 7단계: 실전 예측!
# ============================================

# 예측 이유 분석 함수
def explain_prediction(game_data):
    """
    예측 이유를 설명하는 함수
    각 특성이 홈팀/원정팀에게 얼마나 유리한지 분석
    """
    reasons = []

    # 각 특성 분석
    home_rating = game_data['home_team_rating'].values[0]
    away_rating = game_data['away_team_rating'].values[0]
    rating_diff = game_data['rating_diff'].values[0]
    recent_form_diff = game_data['recent_form_diff'].values[0]
    home_wins = game_data['home_team_wins_last_10'].values[0]
    away_wins = game_data['away_team_wins_last_10'].values[0]
    home_points = game_data['home_team_avg_points'].values[0]
    away_points = game_data['away_team_avg_points'].values[0]

    # 능력치 비교
    if rating_diff > 5:
        reasons.append(f"홈팀 능력치가 {rating_diff}점 높음 (홈: {home_rating} vs 원정: {away_rating})")
    elif rating_diff < -5:
        reasons.append(f"원정팀 능력치가 {abs(rating_diff)}점 높음 (원정: {away_rating} vs 홈: {home_rating})")
    else:
        reasons.append(f"양팀 능력치 비슷함 (홈: {home_rating} vs 원정: {away_rating})")

    # 최근 폼 비교
    if recent_form_diff > 2:
        reasons.append(f"홈팀 최근 폼이 좋음 (최근 10경기: 홈 {home_wins}승 vs 원정 {away_wins}승)")
    elif recent_form_diff < -2:
        reasons.append(f"원정팀 최근 폼이 좋음 (최근 10경기: 원정 {away_wins}승 vs 홈 {home_wins}승)")
    else:
        reasons.append(f"양팀 최근 폼 비슷함 (최근 10경기: 홈 {home_wins}승 vs 원정 {away_wins}승)")

    # 평균 득점 비교
    points_diff = home_points - away_points
    if points_diff > 5:
        reasons.append(f"홈팀 공격력이 우수함 (평균 득점: 홈 {home_points}점 vs 원정 {away_points}점)")
    elif points_diff < -5:
        reasons.append(f"원정팀 공격력이 우수함 (평균 득점: 원정 {away_points}점 vs 홈 {home_points}점)")

    # 홈 어드밴티지
    reasons.append("홈 어드밴티지 효과 (홈팬 응원, 익숙한 코트)")

    return reasons

print("="*60)
print("[7단계] 실전 경기 예측!")
print("="*60)

# 예측할 경기 설정
new_games = pd.DataFrame({
    'home_team_rating': [88, 92, 85],
    'away_team_rating': [85, 90, 88],
    'home_team_wins_last_10': [7, 8, 5],
    'away_team_wins_last_10': [6, 7, 7],
    'home_team_avg_points': [112, 115, 108],
    'away_team_avg_points': [110, 113, 110],
    'home_advantage': [1, 1, 1],
    'rating_diff': [3, 2, -3],
    'recent_form_diff': [1, 1, -2]
})

game_names = [
    "Lakers (홈) vs Warriors (원정)",
    "Celtics (홈) vs Nets (원정)",
    "Heat (홈) vs Bucks (원정)"
]

predictions = model.predict(new_games)
probabilities = model.predict_proba(new_games)

print("\n경기 예측 결과:\n")
for i, (game, pred, prob) in enumerate(zip(game_names, predictions, probabilities)):
    winner = "홈팀 승!" if pred == 1 else "원정팀 승!"
    confidence = prob[pred] * 100

    print(f"{i+1}. {game}")
    print(f"   예측: {winner}")
    print(f"   확신도: {confidence:.1f}%")
    print(f"   확률: 홈팀 {prob[1]*100:.1f}% vs 원정팀 {prob[0]*100:.1f}%")

    # 예측 이유 출력
    print(f"   예측 이유:")
    game_data = new_games.iloc[[i]]
    reasons = explain_prediction(game_data)
    for reason in reasons:
        print(f"     - {reason}")
    print()

# ============================================
# 8단계: 모델 저장 (선택사항)
# ============================================
print("="*60)
print("[8단계] 모델 저장")
print("="*60)

import pickle

# 모델 저장
with open('nba_prediction_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("[완료] 모델 저장 완료: nba_prediction_model.pkl")
print("\n나중에 이 모델을 불러와서 새로운 경기 예측 가능!")
print()

# ============================================
# 프로젝트 완료!
# ============================================
print("="*60)
print("[완료] NBA 경기 예측 프로젝트 완료!")
print("="*60)
print()
print("[완료한 것]")
print("  1. 데이터 준비 및 분석")
print("  2. 머신러닝 모델 학습 (Random Forest)")
print("  3. 모델 평가 (정확도, 특성 중요도)")
print("  4. 실전 경기 예측")
print("  5. 모델 저장")
print()
print("[다음 단계]")
print("  - 실제 NBA API에서 데이터 가져오기")
print("  - 더 많은 특성 추가 (선수 부상, 백투백 경기 등)")
print("  - 다른 모델 시도 (XGBoost, Neural Network)")
print("  - 웹 앱으로 만들기")
print()

# ============================================
# 9단계: 홈/원정 비교 분석 (홈 어드밴티지 효과)
# ============================================
print("="*60)
print("[9단계] 홈/원정 비교 분석 - 홈 어드밴티지 효과 확인")
print("="*60)
print()

# 같은 두 팀이 홈/원정을 바꿔서 경기할 때 어떻게 달라질까?
print("시나리오: Lakers vs Warriors (능력치는 동일, 홈/원정만 변경)")
print("-"*60)

# 경기 1: Lakers 홈 vs Warriors 원정
game1 = pd.DataFrame({
    'home_team_rating': [88],
    'away_team_rating': [85],
    'home_team_wins_last_10': [7],
    'away_team_wins_last_10': [6],
    'home_team_avg_points': [112],
    'away_team_avg_points': [110],
    'home_advantage': [1],
    'rating_diff': [3],
    'recent_form_diff': [1]
})

# 경기 2: Warriors 홈 vs Lakers 원정 (홈/원정 반대)
game2 = pd.DataFrame({
    'home_team_rating': [85],        # Warriors가 홈
    'away_team_rating': [88],        # Lakers가 원정
    'home_team_wins_last_10': [6],
    'away_team_wins_last_10': [7],
    'home_team_avg_points': [110],
    'away_team_avg_points': [112],
    'home_advantage': [1],
    'rating_diff': [-3],             # 능력치 차이 반대
    'recent_form_diff': [-1]         # 최근 폼 차이 반대
})

pred1 = model.predict(game1)[0]
prob1 = model.predict_proba(game1)[0]

pred2 = model.predict(game2)[0]
prob2 = model.predict_proba(game2)[0]

print("\n경기 1: Lakers (홈) vs Warriors (원정)")
print(f"  Lakers 능력치: 88, Warriors 능력치: 85")
print(f"  예측: {'Lakers 승!' if pred1 == 1 else 'Warriors 승!'}")
print(f"  확률: Lakers {prob1[1]*100:.1f}% vs Warriors {prob1[0]*100:.1f}%")
print(f"  예측 이유:")
reasons1 = explain_prediction(game1)
for reason in reasons1:
    print(f"    - {reason}")
print()

print("경기 2: Warriors (홈) vs Lakers (원정)")
print(f"  Warriors 능력치: 85, Lakers 능력치: 88")
print(f"  예측: {'Warriors 승!' if pred2 == 1 else 'Lakers 승!'}")
print(f"  확률: Warriors {prob2[1]*100:.1f}% vs Lakers {prob2[0]*100:.1f}%")
print(f"  예측 이유:")
reasons2 = explain_prediction(game2)
for reason in reasons2:
    print(f"    - {reason}")
print()

print("분석:")
print(f"  홈 어드밴티지 효과로 인해 예측 확률이 변경되었습니다!")
print(f"  Lakers가 홈일 때: Lakers 승률 {prob1[1]*100:.1f}%")
print(f"  Warriors가 홈일 때: Lakers 승률 {prob2[0]*100:.1f}%")
print(f"  홈 어드밴티지 영향: {abs(prob1[1] - prob2[0])*100:.1f}%p 차이")
print()

# 능력치가 동일한 경우
print("-"*60)
print("시나리오 2: 능력치가 완전히 동일한 두 팀 (Celtics vs Heat)")
print("-"*60)

game3 = pd.DataFrame({
    'home_team_rating': [85],
    'away_team_rating': [85],
    'home_team_wins_last_10': [7],
    'away_team_wins_last_10': [7],
    'home_team_avg_points': [110],
    'away_team_avg_points': [110],
    'home_advantage': [1],
    'rating_diff': [0],
    'recent_form_diff': [0]
})

game4 = pd.DataFrame({
    'home_team_rating': [85],
    'away_team_rating': [85],
    'home_team_wins_last_10': [7],
    'away_team_wins_last_10': [7],
    'home_team_avg_points': [110],
    'away_team_avg_points': [110],
    'home_advantage': [1],
    'rating_diff': [0],
    'recent_form_diff': [0]
})

pred3 = model.predict(game3)[0]
prob3 = model.predict_proba(game3)[0]

print("\n경기 3: Celtics (홈) vs Heat (원정) - 모든 능력치 동일")
print(f"  예측: {'Celtics 승!' if pred3 == 1 else 'Heat 승!'}")
print(f"  확률: 홈팀 {prob3[1]*100:.1f}% vs 원정팀 {prob3[0]*100:.1f}%")
print(f"  예측 이유:")
reasons3 = explain_prediction(game3)
for reason in reasons3:
    print(f"    - {reason}")
print()

print("결론:")
print(f"  능력치가 동일할 때도 홈팀이 {prob3[1]*100:.1f}% 승률을 가집니다!")
print(f"  홈 어드밴티지는 NBA 예측에서 매우 중요한 요소입니다.")
print()

print("="*60)
