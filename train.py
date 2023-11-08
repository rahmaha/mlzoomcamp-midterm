import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error

import xgboost as xgb
from xgboost import XGBRegressor


# data preparation
data_path = '.\midterm-project\data\diamonds.csv'
df = pd.read_csv(data_path)

# will only use carat, color, clarity and cut feature
categorical = ['cut', 'color', 'clarity']
numerical = ['carat']

price_logs = np.log1p(df.price)

# split
df_full_train, df_test = train_test_split(
    df[categorical+numerical+['price']], test_size=0.2, random_state=42)
df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = np.log1p(df_full_train.price.values)
y_test = np.log1p(df_test.price.values)

del df_full_train['price']
del df_test['price']

# model
train_dicts = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

xgb_model = XGBRegressor(random_state=42,
                         eta=0.1,
                         max_depth=10,
                         n_jobs=-1)
xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_pred, y_test))
print('rmse: ', rmse)

with open(".\midterm-project\model.bin", "wb") as file_out:
    pickle.dump(xgb_model, file_out)

with open(".\midterm-project\dv.bin", "wb") as file_out:
    pickle.dump(dv, file_out)
