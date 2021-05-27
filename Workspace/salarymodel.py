import pandas

ds = pandas.read_csv('Salary_Data.csv')

x = ds['YearsExperience']

x = x.values

x = x.reshape(30,1) 

y = ds['Salary']

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x , y)

model.coef_

import joblib

joblib.dump(model, 'salaryprediction.pk1')
