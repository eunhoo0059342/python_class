import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 1️⃣ Tkinter root 숨기기
root = Tk()
root.withdraw()

# 2️⃣ CSV 파일 선택
file_path = askopenfilename(
    title="CSV 파일을 선택하세요",
    filetypes=[("CSV files", "*.csv")]
)
if not file_path:
    raise FileNotFoundError("CSV 파일을 선택하지 않았습니다.")

# 3️⃣ CSV 읽기
df = pd.read_csv(file_path, encoding="utf-8")  # 필요시 cp949
print("원본 데이터 컬럼:", df.columns.tolist())

# 4️⃣ 컬럼 변환
# player_sum -> sumofcards
df['player_sum'] = df['sumofcards']

# dealer_card -> sumofdeal
df['dealer_card'] = df['sumofdeal']

# has_ace -> 첫 두 카드에 A가 있는지 확인
df['has_ace'] = df[['card1', 'card2']].apply(lambda x: int('A' in x.values), axis=1)

# next_sum -> 다음 행의 sumofcards (마지막 행은 동일값으로 처리)
df['next_sum'] = df['sumofcards'].shift(-1).fillna(df['sumofcards'].iloc[-1])

# 확인
print("변환 후 데이터 샘플:")
print(df[['player_sum', 'dealer_card', 'has_ace', 'next_sum']].head())

# 5️⃣ 입력/출력 정의
X = df[['player_sum', 'dealer_card', 'has_ace']].values.astype(float)
y = df['next_sum'].values.astype(float)

# 6️⃣ 데이터 분리 및 스케일링
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7️⃣ 딥러닝 모델 정의
model = Sequential([
    Dense(64, input_dim=3, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 8️⃣ 모델 학습
history = model.fit(
    X_train_scaled, y_train,
    epochs=100,
    batch_size=16,
    validation_split=0.1,
    verbose=1
)

# 9️⃣ 테스트 손실 확인
test_loss = model.evaluate(X_test_scaled, y_test)
print("테스트 손실(MSE):", test_loss)

# 10️⃣ 모델 저장
model.save("blackjack_model.h5")
print("사전 학습된 모델이 'blackjack_model.h5'로 저장되었습니다.")
