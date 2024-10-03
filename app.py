# from warnings import resetwarnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


xlsx = pd.ExcelFile('homeprices.xlsx')

df = xlsx.parse('sheet1')
# print(df[['area']])
# print(df.price)

plt.scatter(df.area, df.price, color='red', marker='+')
plt.xlabel('area')
plt.ylabel('price')
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()

# #linear
# reg = linear_model.LinearRegression()
# reg.fit(df[['area']], df.price)

# reg.predict([[2600]])

d = xlsx.parse('sheet2')
print(d.head())

p = reg.predict(d)

d['prices'] = p

print(d)
d.to_excel('predictions.xlsx')
# y = k*x + b
# reg.coef_ # k
# reg.intercept_ # b
# y = 135.78767123*3300 + 180616.43835616432
# print(y)
