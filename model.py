import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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


lr = LinearRegression()
lr.fit(X_train, y_train)


y_pred = lr.predict(X_test)


mae = np.mean(np.abs(y_test - y_pred))   
print(mae)

with open('model.pkl', 'wb') as f:
    pickle.dump(lr, f)

with open('column_transformer.pkl', 'wb') as f:
    pickle.dump(ct, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(sc, f)