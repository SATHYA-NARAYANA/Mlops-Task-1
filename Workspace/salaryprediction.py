import os
os.system("tput setaf 1")
print("\t\t\t\t Welcome ")
os.system("tput setaf 7")
print("\t\t\t------------------------")
name = input('Enter employee name : ')
import joblib
num = float(input('Enter year of experience : '))
model = joblib.load('salaryprediction.pk1')
print()
print('Name               : ' ,name)
print('Year_of_Experience : ', num)
output = model.predict([[num]])
print('Here is Prediction result: ' ,int(output))
