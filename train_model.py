import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv("smart_house.csv")

X = df[['Area', 'Bedrooms', 'Bathrooms', 'Location']]
y = df['Price']

preprocessor = ColumnTransformer(transformers=[
    ('loc', OneHotEncoder(), ['Location'])
], remainder='passthrough')

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print ("model working")