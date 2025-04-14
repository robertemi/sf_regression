import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Dropout
from tensorflow.keras.regularizers import l2

df = pd.read_csv('leads.csv')
X = df.drop(columns=['Name', 'Company', 'Probability'])
y = df['Probability']

cathegorical_features = ['Status', 'Rating', 'Source']

ct = ColumnTransformer([('encoder', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), cathegorical_features)], remainder='passthrough')
X = ct.fit_transform(X)
X = pd.DataFrame(X)


sc = StandardScaler()
X = sc.fit_transform(X)
X = pd.DataFrame(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = Sequential()
model.add(Input(shape=(X.shape[1],)))

model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.01)))
BatchNormalization()
Dropout(0.3)

model.add(Dense(16, activation='relu'))

model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.01)))
BatchNormalization()
Dropout(0.3)


model.add(Dense(16, activation='relu'))

model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.01)))
BatchNormalization()
Dropout(0.3)

model.add(Dense(16, activation='relu'))

model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.01)))
BatchNormalization()
Dropout(0.3)

model.add(Dense(1, activation='linear'))

model.compile(optimizer='adam', loss='mse', metrics=['root_mean_squared_error'])

results = model.fit(
    X_train, y_train,
    batch_size=32,
    epochs=100,
    validation_split=0.2
)

y_pred = model.predict(X_test)

history_df = pd.DataFrame.from_dict(results.history)
fig, ax1 = plt.subplots(figsize=(10, 7))

ax1.plot(history_df.index, history_df['loss'], label='Train Loss', color='blue', linestyle='-')
ax1.plot(history_df.index, history_df['val_loss'], label='Validation Loss', color='green', linestyle='--')
ax1.set_ylabel('Loss')
ax1.set_xlabel('Epochs')
ax1.set_yscale('log')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)


ax2 = ax1.twinx()
ax2.plot(history_df.index, history_df['root_mean_squared_error'], label='Train RMSE', color='orange', linestyle='-')
ax2.plot(history_df.index, history_df['val_root_mean_squared_error'], label='Validation RMSE', color='red', linestyle='--')
ax2.set_ylabel('Root Mean Squared Error')
ax2.legend(loc='upper right')

plt.title("Training Progress: Loss & RMSE Over Epochs")
plt.show()